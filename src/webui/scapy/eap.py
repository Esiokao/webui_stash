from scapy.all import *


# EAPOL Start packet
def send_eapol_start(interface):
    eapol_start = (
        Ether(dst="01:80:C2:00:00:03", src="00:11:22:33:44:55", type=0x888E) /
        EAPOL(version=1, type=1))
    sendp(eapol_start, iface=interface)


if __name__ == "__main__":
    interface = "eth1"  # Replace with your network interface
    send_eapol_start(interface)
