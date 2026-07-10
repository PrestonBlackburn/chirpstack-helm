# Script to test the gateway bridge can be reached

import socket, struct, random

HOST = "chirpgateway.lan"
PORT = 1700

token = random.randint(0, 65535)
gateway_eui = bytes.fromhex("AA555A0000000001")  # fake EUI, 8 bytes

# PULL_DATA packet: version(1) + token(2) + identifier(1=0x02) + gwEUI(8)
packet = struct.pack(">BH B", 2, token, 2) + gateway_eui

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(3)
sock.sendto(packet, (HOST, PORT))

try:
    data, addr = sock.recvfrom(1024)
    print("Got response from", addr, data.hex())
    if len(data) >= 4 and data[3] == 4:
        print("PULL_ACK received — bridge is reachable and responding correctly!")
except socket.timeout:
    print("No response — check firewall/LB routing/pod readiness")