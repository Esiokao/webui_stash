import asyncio
import os
import sys
import threading
import time
from collections import deque  # ✅ used for fixed-size response buffer

import serial
from colorama import Fore, init
from prompt_toolkit import PromptSession
from prompt_toolkit.key_binding import KeyBindings

init(autoreset=True)


class SerialEnv:
    # Adapter to mimic SecureCRT environment
    def __init__(self, baudrate: int = None, port: str = None, use_mock: bool = None):
        # 優先取用傳入參數，若無則從環境變數讀取，最後再給預設值
        env_use_mock = os.getenv("USE_MOCK", "false").lower() in ("true", "1", "yes")
        self.use_mock = use_mock if use_mock is not None else env_use_mock

        env_port = os.getenv("COM_PORT", "COM9")
        actual_port = port if port is not None else env_port
        self.port = "loop://" if self.use_mock else actual_port

        env_baudrate = int(os.getenv("BAUD_RATE", "115200"))
        self.baudrate = baudrate if baudrate is not None else env_baudrate
        self.queue = asyncio.Queue()
        self.serial = None
        self.running = True
        self.last_received = ""
        self.last_sent = ""
        self.history = []
        self.buffer = deque(maxlen=5)  # ✅ keep only the last 5 responses
        self.defer_time = 0.05

        # Async prompt input & key binding
        self.session = PromptSession()
        self.bindings = KeyBindings()

        @self.bindings.add("tab")
        def _(event):
            """Send current input with \\t on Tab press."""
            echo = False  # dont
            current_text = event.app.current_buffer.text
            self.send(current_text + "\t", echo)

        self.simulator = None
        self.init_serial()

        # 如果啟用 mock 或連線失敗，降級為 MockSwitchSimulator
        if self.serial is None or self.use_mock:
            from webui.mock.switch_simulator import MockSwitchSimulator
            self.use_mock = True
            self.simulator = MockSwitchSimulator()
            print("💡 Running in Mock Switch Simulator mode.")
            self.running = True
            return

        # Start background thread to read serial data
        self.read_thread = threading.Thread(target=self._read_serial, daemon=True)
        self.read_thread.start()

    def init_serial(self):
        """Initialize serial connection."""
        if self.use_mock:
            self.serial = None
            return

        try:
            self.serial = serial.serial_for_url(self.port, baudrate=self.baudrate, timeout=1)
            print(f"✅ Serial connected on {self.port}, baud rate {self.baudrate} established")
        except Exception as e:
            print(f"❌ Serial connection failed: {e}. Falling back to Mock Simulator.")
            self.serial = None

    def send(self, data: str, echo: bool = True):
        """Send data over serial and immediately print it."""
        self.last_sent = data
        if echo and data != "":
            sys.stdout.write(f"{Fore.RED}{data}\n")

        if self.use_mock and self.simulator:
            resp = self.simulator.execute_command(data)
            self.last_received = resp
            self.buffer.append(resp)
            self.queue.put_nowait(resp)
            return

        if self.serial:
            byte_str = (data + "\n").encode() if data != "\n" else data.encode()
            self.serial.write(byte_str)
            time.sleep(self.defer_time)

    def waitForString(self, target: str, timeout: int = 150):
        """
        Blocks until the specified string appears in the last 5 responses, or until timeout (in seconds).

        :param target: The string to wait for.
        :param timeout: Timeout duration in seconds.
        :return: The matching response string.
        :raises TimeoutError: If target string is not received within the timeout.
        """
        end_time = time.time() + timeout

        while time.time() < end_time:
            combined = "".join(self.buffer)
            if target in combined:
                return target
            time.sleep(self.defer_time)

        raise TimeoutError(f"⏱ Timeout after {timeout}s: '{target}' not found in recent responses.")

    def _read_serial(self):
        """Background thread to continuously read incoming serial data."""
        while self.running:
            if not self.serial:
                continue

            try:
                if not self.serial.in_waiting:
                    continue
                data = self.serial.readline()
                decoded = data.decode(errors="ignore")
                # to ignore same return string from the serial port
                if decoded.strip() == self.last_sent.strip():
                    continue

                self.last_received = decoded
                self.buffer.append(decoded)  # ✅ Add new line to rolling buffer

                sys.stdout.write(f"{decoded}")

            except Exception as e:
                sys.stdout.write(f"\n⚠ Error reading serial: {e}")
                sys.stdout.flush()

    async def get_next_message(self):
        """Asynchronously get next message from queue (mock only)."""
        return await self.queue.get()

    def close(self):
        """Cleanly close the serial connection."""
        self.running = False
        if self.serial:
            self.serial.close()
        print("\n🔌 Serial closed")

    # user input handler
    async def user_input_loop(self):
        """Handle async user input from terminal with tab-completion support."""
        echo = False
        while True:
            try:
                data = await self.session.prompt_async(key_bindings=self.bindings)
                data = data.strip()
                if data.lower() == "exit":
                    print("👋 Exiting program...")
                    self.close()
                    break
                self.send(data, echo)
            except (EOFError, KeyboardInterrupt):
                print("\n🚪 Exit by user interrupt")
                self.close()
                break

    def sleep(self, timeout_time: int):
        """Delay execution for a given duration in seconds."""
        time.sleep(timeout_time)
