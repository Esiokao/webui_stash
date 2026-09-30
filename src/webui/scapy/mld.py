from scapy.all import *
import math

for byte2 in range(5):
    for byte1 in range(128):
        byte3_str = "%02x" % math.floor(byte1 / 256)
        byte2_str = "%02x" % (byte2 % 256)
        byte1_str = "%02x" % (byte1 % 256)
        mgrp_str = "%03x" % byte1
        dst_str = "33:33:00:" + byte3_str + ":" + byte2_str + ":" + byte1_str
        mgrp_addr_str = "ff13::" + byte2_str + byte1_str
        mgrp_addr_str_2 = "FF05::" + mgrp_str
        eth = Ether(dst=dst_str, src="00:11:22:33:44:55", type=0x86dd)
        ipv6_hdr = IPv6(src="fe80::dead:bee5", dst=mgrp_addr_str, hlim=1)
        hbh = IPv6ExtHdrHopByHop(options=RouterAlert())
        mld_report = ICMPv6MLReport(mladdr=mgrp_addr_str_2)
        packet = eth / ipv6_hdr / hbh / mld_report
        packet.show()
        sendp(packet, iface="eth1")
