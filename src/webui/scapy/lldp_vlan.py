from scapy.all import *

from generate_mac import generate_mac
import random
import math
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


def random_hex(prefix):
    """
  隨機產生一位數的 16 進位制字串並加上指定前綴。

  Args:
    prefix: 字串前綴。

  Returns:
    隨機產生的 16 進位制字串。
  """

    hex_digits = "0123456789ABCDEF"
    return prefix + random.choice(hex_digits)


def lldp_med():

    # data = 'helloworld'

    # mac_src = "28:10:7B:00:00:00"

    # temp = Ether(src=mac_src) / \

    #      LLDPDU() / IP(ttl=10)

    # src_mac = '0A:AA:1c:00:12:35'

    # dst_mac = '01:80:c2:00:00:0e'

    # eth = Ether(src=src_mac, dst=dst_mac)

    # chassis_id = LLDPDUChassisID(subtype=0x04, id=src_mac)

    # port_id = LLDPDUPortID(subtype=0x05, id='2')

    # ttl = LLDPDUTimeToLive(ttl=100)

    # vlanID = Dot1Q(vlan=0)

    # frame = eth / vlanID / chassis_id / port_id / ttl

    # sendp(frame, iface='eth1', count=4)

    # print(frame.show())
    ####
    def genFrameThenSend(mac_src, digi_front, digi_rear):

        chassis = bytearray(7)

        #chassis[0:3] = (0x02,0x06,0x07)

        chassis[0:3] = (0x02, 0x07, 0x04)

        chassis[3:] = (0x94, 0xf1, 0x28, 0x8b, digi_front, digi_rear)

        # chassis[3:] = str.encode('94:f1:28:8b:aa:1e', 'utf-8')
        # print(str.encode('94:f1:28:8b:aa:1e', 'utf-8'))

        # Sysname

        sysname = bytearray(7)

        sysname[0:2] = (0x0a, 0x0c)

        sysname[2:] = str.encode('FakeSwitch01', 'utf-8')

        # Sys Description

        sysdesc = bytearray(12)

        sysdesc[0:2] = (0x0c, 0x3f)

        # sysdesc[2:] = str.encode(
        #     'Aruba JL258A 2930F-8G-PoE+-2SFP+ Switch, revision WC.16.10.0015, ROM WC.16.01.0008 (/ws/swbuildm/rel_ajanta_qaoff/code/build/lvm(swbuildm_rel_ajanta_qaoff_rel_ajanta))',
        #     'utf-8')
        sysdesc[2:] = str.encode(
            str('DXS-1210-10TS 10GbE Smart Managed Switch Rev.B1/V2.02.003(Test)'
                ), 'utf-8')

        # Management address
        mgmtaddr = bytearray(7)

        mgmtaddr[0:2] = (0x10, 0x0c)

        mgmtaddr[2:] = (0x05, 0x01, 0x0a, 0x01, 0x01, 0x08, 0x02, 0x00, 0x00,
                        0x00, 0x00, 0x00)

        #portID = bytearray( (0x04,0x07,0x03, 0x00,0x01,0x02,0xff,0xfe,0xfd) ) # fake MAC address

        # Port ID

        portID = bytearray((0x04, 0x02, 0x07, 0x32))

        # Build TTL

        TTL = bytearray((0x06, 0x02, 0x00, 0x78))

        # Build capabilities

        cap = bytearray(7)

        cap[0:2] = (0x0e, 0x04)

        cap[2:] = (0x00, 0x14, 0x00, 0x14)

        # Vendor specific attributes

        vendor = bytearray(7)

        vendor[0:2] = (0xfe, 0x06)

        vendor[2:] = (0x00, 0x16, 0xb9, 0x02, 0x00, 0x00)

        # Port description

        portdescr = bytearray((0x08, 0x01, 0x35))

        # LLDP/MED capabilities

        med = bytearray(7)

        med[0:2] = (0xfe, 0x07)

        med[2:] = (0x00, 0x12, 0xbb, 0x01, 0x00, 0x0f, 0x04)

        # LLDP/MED network policy

        networkPolicy = bytearray(10)

        networkPolicy[0:2] = (0xfe, 0x08)

        networkPolicy[2:5] = (0x00, 0x12, 0xbb)

        # Media SubType
        networkPolicy[5:7] = (0x02, 0x01)

        # Application Type
        # networkPolicy[6:7] = (0x01)
        # Vlan ID
        networkPolicy[7:] = (0x00, 0x05, 0x04)

        # Local PVID

        portvlan = bytearray(7)

        portvlan[0:2] = (0xfe, 0x06)

        portvlan[2:] = (0x00, 0x80, 0xc2, 0x01, 0x00, 0x01)

        # End padding

        end = bytearray((0x00, 0x00))

        # Build payload

        payload = bytes(chassis + portID + TTL + sysname + sysdesc + cap +
                        mgmtaddr + vendor + portdescr + med + networkPolicy +
                        portvlan + end)

        #LLDP multicast address

        mac_lldp_multicast = '01:80:c2:00:00:0e'

        # Build frame

        # eth = Ether(src='94:f1:28:8b:aa:21', dst=mac_lldp_multicast, type=0x88cc)
        eth = Ether(src=mac_src, dst=mac_lldp_multicast, type=0x88cc)
        frame = eth / Raw(
            load=bytes(payload)) / Padding(b'\x00\x00\x00\x00') / Dot1Q(vlan=2)

        # frame length should be 60, minimum Ethernet frame length

        # Output packet to console
        frame.show()
        # Send packet. To get proper interface run getmac/v on Windows (escape your slashes) OR ip a s eth0 on Linux

        sendp(frame, loop=10, count=1, verbose=1, iface="eth1")

    for i in range(5000):
        head = math.floor(i / 256)
        rear = i % 256
        digi_front = head
        digi_rear = rear
        # mac_src = generate_mac.vid_provided("00:" + random_hex.random_hex("") +
        #                                     random_hex.random_hex("") + ":" +
        #                                     random_hex.random_hex("") +
        #                                     random_hex.random_hex(""))

        # mac_src = "0A:E0:AA:" + format(_, 'x')
        macSrcPrefix = '90:94:E4:8b:'
        mac_src = macSrcPrefix + to_hex_string(head) + ":" + to_hex_string(
            rear)

        genFrameThenSend(mac_src, digi_front, digi_rear)


def to_hex_string(number):
    # "%02x" % number
    hex_string = format(number, '02x')
    return hex_string


if __name__ == '__main__':

    lldp_med()
