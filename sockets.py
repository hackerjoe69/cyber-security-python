import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(client)
client.connect(('youtube.com', 80)) # Http

client.send(b"GET / HTTP/1.1\r\nHOST: google.com\r\n\r\n")

response = client.recv(4096)

print(response.decode())
client.close()