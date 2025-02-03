import socket

sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.ntohs(3))

while True:
    raw_packet, addr = sniffer.recvfrom(65536)
    print(f'Packet received from {addr}: {raw_packet}')
