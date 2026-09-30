import socket
import pytest
import os
from dotenv import load_dotenv

load_dotenv("Settings.env")

http_port = os.getenv("HTTP_PORT")
tls_port = os.getenv("TLS_PORT")
switch_ip_address = os.getenv("SWITCH_IP_ADDRESS")


def is_ip_reachable(ip, port, timeout=3):
    """檢查 IP 是否可以連線"""
    try:
        with socket.create_connection((ip, port), timeout):
            return True
    except (socket.timeout, socket.error):
        return False


@pytest.mark.parametrize(
    "ip, port",
    [
        # (switch_ip_address, tls_port),
        (switch_ip_address, http_port),
    ],
)
def test_ip_connectivity(ip, port):
    assert is_ip_reachable(ip, port), f"無法連接到 {ip}:{port}"
