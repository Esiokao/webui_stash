from scapy.all import *

class TWAMP(Packet):
    name = "TWAMP"
    fields_desc = [
        IntField("session_id", 0),   # Example session ID field
        ByteField("msg_type", 1),    # Message type, adjust based on TWAMP spec
        IntField("seq_num", 1),      # Sequence number field
        IntField("timestamp", 0),    # Placeholder for timestamp, if required
        # Add more fields as needed according to TWAMP specifications
    ]

# Bind the TWAMP layer to UDP
bind_layers(UDP, TWAMP, dport=12345)

# Define the parameters
local_ip = "10.90.90.17"
server_ip = "10.90.90.90"
server_port = 12345  # Set to the UDP port on the D-Link server
session_id = 1       # Example session ID
packet_count = 10    # Number of packets to send

# Send TWAMP packets
for i in range(packet_count):
    # Construct IP layer
    ip = IP(src=local_ip, dst=server_ip)
    
    # Construct UDP layer
    udp = UDP(sport=12345, dport=server_port)
    
    # Construct TWAMP layer with custom fields
    twamp_packet = TWAMP(session_id=session_id, msg_type=1, seq_num=i, timestamp=int(time.time()))
    
    # Combine layers
    packet = ip / udp / twamp_packet

    # Send the packet
    send(packet, iface="eth1")  # Make sure 'eth1' is the correct interface

print(f"Sent {packet_count} TWAMP packets from {local_ip} to {server_ip}.")