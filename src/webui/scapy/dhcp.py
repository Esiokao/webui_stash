
from scapy.all import *

from webui.scapy.utils.randomIP import randomIP as randIP
from webui.scapy.utils.randomMac import random_mac as randMac


def send_dhcp_discover():
    # 創建 Ethernet 層
    # ether = Ether(dst="ff:ff:ff:ff:ff:ff", src=RandMAC(), type=0x0800)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff", src="00:AA:BB:CC:DD:FF", type=0x0800)

    # 創建 IP 層
    ip = IP(src="10.90.90.250", dst="255.255.255.255")

    # 創建 UDP 層
    udp = UDP(sport=68, dport=67)

    # 創建 BOOTP 層
    bootp = BOOTP(chaddr=[RandMAC().replace(":", "")], xid=RandInt(), flags=0x8000)

    # 創建 DHCP 層
    dhcp = DHCP(options=[("message-type", "discover"), "end"])

    # 將所有層結合在一起
    dhcp_discover = ether / ip / udp / bootp / dhcp

    # 發送 DHCP Discover 包
    sendp(dhcp_discover)


def send_dhcp_offer(client_mac, client_ip, server_ip, server_mac, vlan_id, iface):
    # 創建 Ethernet 層
    ether = Ether(dst=client_mac, src=server_mac)

    # 添加 802.1Q VLAN 層
    dot1q = Dot1Q(vlan=vlan_id)

    # 創建 IP 層
    ip = IP(src=server_ip, dst="255.255.255.255")

    # 創建 UDP 層
    udp = UDP(sport=67, dport=68)

    # 創建 BOOTP 層
    bootp = BOOTP(op=2, yiaddr=client_ip, siaddr=server_ip, chaddr=client_mac.replace(":", ""))

    # 創建 DHCP 層
    dhcp = DHCP(
        options=[
            ("message-type", "offer"),
            ("server_id", server_ip),
            ("lease_time", 86400),
            ("subnet_mask", "255.255.255.0"),
            ("router", server_ip),
            ("name_server", server_ip),
            "end",
        ]
    )

    # 將所有層結合在一起
    dhcp_offer = ether / dot1q / ip / udp / bootp / dhcp

    # 發送 DHCP Offer 封包
    sendp(dhcp_offer, iface=iface, verbose=False)
    print(f"DHCP Offer sent to {client_mac} on VLAN {vlan_id} via {iface}, offering IP {client_ip}")


if __name__ == "__main__":
    ATTEMPT_TIMES = 4000
    for _ in range(ATTEMPT_TIMES):
        # 設定客戶端 MAC 地址、客戶端 IP、服務器 IP 和服務器 MAC 地址
        # client_mac = "00:11:22:33:44:55"
        client_mac = randMac()
        # client_ip = "192.168.0.100"
        client_ip = randIP()
        # server_ip = "192.168.10.101"
        server_ip = randIP()
        # server_mac = "66:77:88:99:aa:bb"  # 這應該是伺服器的實際 MAC 地址
        server_mac = randMac()  # 這應該是伺服器的實際 MAC 地址
        vlan_id = random.randint(1, 4094)  # 設置 VLAN ID
        iface = "eth1"  # 設定網絡接口

        send_dhcp_offer(client_mac, client_ip, server_ip, server_mac, vlan_id, iface)
    # send_dhcp_discover()
