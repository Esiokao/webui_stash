from scapy.all import Ether, IP, UDP, sendp
import random
import time

# mac flapping

# MAC Flapping 封包是指在網路中，同一個 MAC 地址在不同的端口間不斷變動的情況，這會導致網路設備（例如交換機）在記錄 MAC 地址與端口映射表時不斷更新，進而產生混亂。這種情況下，MAC 地址的學習表會頻繁更改，稱之為「MAC 地址翻動」（MAC Flapping）。

# 設定固定的源 MAC 地址和 IP 地址
src_mac = "AA:BB:CC:DD:EE:FF"
dst_mac = "FF:EE:DD:CC:BB:AA"  # 目標 MAC 地址
src_ip = "10.90.90.14"          # 本機 IP
dst_ip = "10.90.90.90"          # 目標 IP

# 設定網卡名稱，需依據實際情況調整
interface = "eth1"
interface2 = "eth4"

# 設定封包的發送次數和間隔
packet_count = 50000
interval = .1  # 每個封包之間的間隔 (秒)

def randMac():
    # 生成隨機的 MAC 地址
    return "08:%02x:%02x:%02x:%02x:%02x" % (random.randint(
        0, 255), random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255), random.randint(0, 255))


for i in range(packet_count):


    # 隨機選擇源端口以模擬 MAC Flapping
    src_port = random.randint(1000, 65535)

    src_mac = randMac()

    # 建立 Ethernet, IP, UDP 封包
    packet = Ether(src=src_mac, dst=dst_mac) / IP(src=src_ip, dst=dst_ip) / UDP(sport=src_port, dport=12345)

    # 發送封包
    sendp(packet, iface=interface, verbose=False)
    print(f"Sent packet {i + 1} with src_port={src_port} via {interface}")

    # 等待指定的間隔時間
    time.sleep(interval)

    # 發送封包
    sendp(packet, iface=interface2, verbose=False)
    print(f"Sent packet {i + 1} with src_port={src_port} via {interface2}")

