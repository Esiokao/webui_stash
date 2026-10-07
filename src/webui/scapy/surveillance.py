
from generate_mac import generate_mac
from scapy.all import *


def fdb_table():

    for _ in range(100):
        # mac_src = generate_mac.vid_provided("00:" + random_hex.random_hex("") +

        #                                     random_hex.random_hex("") + ":" +

        #                                     random_hex.random_hex("") +

        #                                     random_hex.random_hex(""))

        # mac_src = "0A:E0:AA:" + format(_, 'x')

        randVoiceVlan = generate_mac.vid_provided("0A:E0:AA:")

        surveillance = generate_mac.vid_provided("F0:7D:69:")

        print(surveillance)
        # mac_src = generate_mac.total_random()
        # print(surveillance)
        pkt = Ether(src=surveillance) / Dot1Q(vlan=2) / IP(dst="10.90.90.90", src="10.90.90.55") / ICMP()
        print(pkt.show())
        sendp(pkt, iface="eth1")


# fdb_table()

# 28:10:7B:00:00:00


def surveillance():
    for _ in range(1000):
        mac_src = "F0:7D:68:00:00:00"
        randVoiceVlan = generate_mac.vid_provided("0A:E0:AA:")

        surveillance = generate_mac.vid_provided("F0:7D:70:")

        print(surveillance)
        # mac_src = generate_mac.total_random()
        # print(surveillance)
        pkt = Ether(src=surveillance, dst="FF:FF:FF:FF:FF:FF") / IP(dst="10.90.90.90", src="10.90.90.55")
        # Dot1Q(vlan=2) / \

        # print(pkt.show())

        sendp(pkt, iface="eth1")


# surveillance()

if __name__ == "__main__":
    # fdb_table()
    # lldp_med()
    surveillance()
