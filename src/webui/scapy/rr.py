from scapy.all import *
from scapy.layers.radius import Radius, RadiusAttribute
from scapy.layers.inet import IP, UDP

# 设置参数
username = 'bob'
password = 'hello'
nas_ipaddr = '192.168.1.1'  # 假设的 NAS IP 地址
radius_server = '10.101.47.37'
shared_secret = 'testing123'

# 创建 Radius 属性
avp1 = RadiusAttribute(type="User-Name", value=username)
avp2 = RadiusAttribute(type="User-Password", value=password)
avp3 = RadiusAttribute(type="NAS-IP-Address", value=nas_ipaddr)

# 创建 Radius 包
radius_packet = Radius(
    code=1, authenticator=RandString(16))  # Access-Request code is 1
radius_packet.add_payload(avp1)
radius_packet.add_payload(avp2)
radius_packet.add_payload(avp3)

# 创建 IP 和 UDP 包
ip_packet = IP(dst=radius_server)
udp_packet = UDP(sport=RandShort(), dport=1812)

# 发送包并接收响应
response = sr1(ip_packet / udp_packet / radius_packet, iface='eth1', timeout=5)

# 打印响应
if response:
    response.show()
else:
    print("No response received")
