from scapy.all import *
import scapy.contrib.igmp
from scapy.contrib.igmpv3 import IGMPv3, IGMPv3mq, IGMP, IGMPv3gr
from scapy.contrib.igmpv3 import IGMPv3mr
import time


def loopDecor(times):

    def decorator(func):

        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)

        return wrapper

    return decorator


@loopDecor(times=500)
def igmpv2():

    #configs
    interfaceName = 'eth1'
    mac_src = "F0:7D:68:00:00:0e"
    mac_dst = "F0:7D:68:00:00:aa"
    randIP = ".".join(str(random.randint(0, 255)) for _ in range(4))

    pkt = Ether(src=mac_src, dst=mac_dst) / \
            IP(dst='10.90.90.1', src='239.255.255.250', tos=0xc0) / \
                scapy.contrib.igmp.IGMP()

    pkt.show()
    sendp(pkt, count=4, iface="eth1")
    # 定義IGMPv2的參數

    # igmp_type = 0x16  # IGMPv2 Membership Report type
    # max_resp_time = 10  # Maximum response time
    # group_address = '224.0.0.1'  # Multicast group address

    # # 創建IP頭
    # ip = IP(dst=group_address)

    # # 創建IGMPv2頭
    # igmp = IGMP(type=igmp_type, gaddr=group_address, mrcode=max_resp_time)

    # # 組合封包
    # packet = ip / igmp

    # # 顯示封包內容
    # packet.show()

    # # 發送封包
    # sendp(packet, iface="eth1")


@loopDecor(times=1)
def igmpv3():
    import random
    randIP = ".".join(str(random.randint(0, 255)) for _ in range(4))
    # susIP = '240.106.219.250'
    # susIP2 = '241.118.91.223'
    # dIP = '240.87.87.87'
    # okIP = '1.2.3.4'
    p_join = Ether(dst='01:00:5e:00:00:16', src='00:0c:29:c8:31:8a') / Dot1Q(
        vlan=1) / IP(src=randIP, dst='224.0.0.22',
                     tos=0xc0) / IGMPv3() / IGMPv3mr(numgrp=1) / IGMPv3gr(
                         rtype=4, maddr="224.0.1.2")
    p_join.show()
    sendp(p_join, count=1, iface='eth1')


if __name__ == "__main__":
    for _ in range(120):
        igmpv2()
        # igmpv3()
        time.sleep(1)
# pass
