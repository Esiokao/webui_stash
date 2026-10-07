# tests/fixtures/serial_fixture.py
import os

import pytest


@pytest.fixture(scope="session")
def serial_env():
    """Serial Port Environment - initializes SerialEnv with COM port or Mock mode."""
    from webui.command.serial_env import SerialEnv

    com_port = os.getenv("COM_PORT", "COM3")
    baud_rate = int(os.getenv("BAUD_RATE", "115200"))
    use_mock = os.getenv("USE_MOCK", "true").lower() in ("true", "1", "yes")

    print(f"\n\n initializing serial env (use_mock={use_mock})")

    env = SerialEnv.SerialEnv(baudrate=baud_rate, port=com_port, use_mock=use_mock)

    yield env

    if env.running:
        try:
            env.close()
        except Exception:
            pass

    print("\n\n tearing down serial env")
