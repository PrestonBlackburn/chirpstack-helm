import socket, json, struct, random, time

GATEWAY_EUI = bytes.fromhex("AA555A0000000001")  # use your registered gateway EUI
BRIDGE_IP = "your-metallb-external-ip"
BRIDGE_PORT = 1700

def push_data(stat=None, rxpk=None):
    token = random.randbytes(2)
    payload = {}
    if stat: payload["stat"] = stat
    if rxpk: payload["rxpk"] = rxpk
    packet = b'\x02' + token + b'\x00' + GATEWAY_EUI + json.dumps(payload).encode()
    sock.sendto(packet, (BRIDGE_IP, BRIDGE_PORT))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Just send gateway stats — enough for ChirpStack to show "last seen"
push_data(stat={
    "time": time.strftime("%Y-%m-%d %H:%M:%S GMT"),
    "rxnb": 0, "rxok": 0, "rxfw": 0, "ackr": 100.0, "dwnb": 0, "txnb": 0
})
print("sent stat packet")