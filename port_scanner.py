import socket

# target = '192.168.158.59' # IP Address
target = input("Enter the IP Address you want to Target: ")
port_length = int(input("Enter the number of ports to scan: "))


for port in range(20, port_length): # [1, 2, 3, 4]  Port You are Scanning
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.5) # Connection Time
    result = client.connect_ex((target, port))

    
    if result == 0:
        print(f'Port {port} is open... ')
        with open('available_ports.txt', 'a') as file:
            file.write(f'Port {port} is open... \n')    
    else:
        print(f"Port {port} is closed")

