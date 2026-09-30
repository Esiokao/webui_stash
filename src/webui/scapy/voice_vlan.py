from scapy.all import Ether, sendp
import random
import time

def generate_random_mac(prefix: str) -> str:
    """
    生成帶有固定前三個字節的隨機 MAC 地址
    :param prefix: 固定的前三個字節前綴（格式如 "12:34:56"）
    :return: 隨機生成的 MAC 地址
    """
    # 確保前綴格式正確（3 個十六進位字節）
    if len(prefix.split(":")) != 3:
        raise ValueError("Prefix must be in the format 'XX:XX:XX' (3 hex bytes)")
    
    # 生成後續隨機的 3 個字節
    random_suffix = ":".join(f"{random.randint(0, 255):02x}" for _ in range(3))
    
    # 拼接完整 MAC 地址
    return f"{prefix}:{random_suffix}"

def send_packet_with_random_mac(prefix: str, iface: str):
    """
    發送帶有固定前三個字節前綴的隨機 MAC 封包
    :param prefix: MAC 地址前三個字節的前綴
    :param iface: 發送封包的網卡介面名稱
    """
    # 生成隨機 MAC 地址
    random_mac = generate_random_mac(prefix)
    print(f"Generated MAC Address: {random_mac}")
    
    # 構造乙太網封包
    packet = Ether(src=random_mac, dst="ff:ff:ff:ff:ff:ff") / b"Random MAC Packet"
    
    # 顯示封包內容
    packet.show()
    
    # 發送封包
    sendp(packet, iface=iface, verbose=True)

# 設定固定前三個字節前綴和網卡名稱
fixed_prefix = "26-14-44".replace('-', ':')  # 你的固定前三個字節
network_interface = "eth1"  # 替換為你的網卡名稱

# 發送封包
for _ in range(5000):
  send_packet_with_random_mac(fixed_prefix, network_interface)
  time.sleep(.05)
