from scapy.all import *
from scapy.layers.radius import RadiusAttribute, Radius


def send_radius_packet(dst_mac, src_mac, dst_ip, username, password,
                       nas_ipaddr, message_type, interface):
    # 創建 Radius 屬性
    avp1 = RadiusAttribute(type="User-Name", value=username)
    avp2 = RadiusAttribute(type="User-Password", value=password)
    # avp3 = RadiusAttribute(type="NAS-IP-Address", value=nas_ipaddr)

    # 創建 Radius 封包
    radius_packet = Radius(
        code=message_type,
        # authenticator=RandString(16),  # 隨機生成 16 字節的 authenticator
        authenticator='testing123',
        id=RandByte())
    radius_packet[Radius].attributes = [avp1, avp2]

    # 建立 Ethernet, IP 和 UDP 封包
    eth_packet = Ether(dst=dst_mac, src=src_mac,
                       type=0x0800)  # 以太網層，type=0x0800 表示 IP
    ip_packet = IP(dst=dst_ip)  # RADIUS 伺服器的目標 IP
    udp_packet = UDP(sport=RandShort(), dport=1812)  # 來源和目標端口

    # 組合封包
    full_packet = eth_packet / ip_packet / udp_packet / radius_packet

    # 發送封包
    sendp(full_packet, iface=interface, verbose=True)


if __name__ == '__main__':
    # for _ in range(1000):
    send_radius_packet(
        dst_mac="ff:ff:ff:ff:ff:ff",  # 目標 MAC 地址
        src_mac="00:aa:bb:cc:dd:ee",  # 來源 MAC 地址
        dst_ip="10.101.47.37",
        username="bob",
        password="hello",
        nas_ipaddr="127.0.1.1",
        message_type=
        "Access-Request",  # 可選：Access-Request, Access-Accept, Access-Reject, Accounting-Request
        interface="eth1")
