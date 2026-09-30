import serial
import asyncio
import threading
import sys
import time
from colorama import Fore, init
from collections import deque  # ✅ used for fixed-size response buffer
from prompt_toolkit import PromptSession
from prompt_toolkit.key_binding import KeyBindings

init(autoreset=True)

class SerialEnv:
    # Adapter to mimic SecureCRT environment
    def __init__(self, baudrate=115200, port="COM9", use_mock=False):
        self.port = "loop://" if use_mock else port
        self.baudrate = baudrate
        self.use_mock = use_mock
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
            echo = False # dont
            current_text = event.app.current_buffer.text
            self.send(current_text + "\t", echo)

        self.init_serial()
        
        # 如果連線失敗，不繼續執行
        if self.serial is None:
            self.running = False
            return  # ⛔️ 停止 init，避免進入 read_thread
        
        # Start background thread to read serial data
        self.read_thread = threading.Thread(target=self._read_serial, daemon=True)
        self.read_thread.start()

    def init_serial(self):
        """Initialize serial connection."""
        try:
            self.serial = serial.serial_for_url(
                self.port, baudrate=self.baudrate, timeout=1
            )
            print(f"✅ Serial connected on {self.port}, baud rate {self.baudrate} established")
        except Exception as e:
            print(f"❌ Serial connection failed: {e}")
            self.serial = None  # ⛔️ None
    

    def send(self, data: str, echo: bool = True):
        """Send data over serial and immediately print it."""
        if self.serial:
            byte_str = (data + '\n').encode() if data != '\n' else data.encode()
            self.last_sent = data
            self.serial.write(byte_str)
            # mimic the user input behavior
            if echo and data != '':
                sys.stdout.write(f"{Fore.RED}{data}\n")  # ✅ Echo sent command
            time.sleep(self.defer_time)

            if self.use_mock:
                mock_response = f"MockResponse: {data}"
                self.queue.put_nowait(mock_response)

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
            combined = ''.join(self.buffer)
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
