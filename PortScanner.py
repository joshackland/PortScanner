import socket
    
def is_port_open(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
   
    if s.connect_ex((ip, int(port))) == 0:
        print(f'{ip}:{port} is OPEN')

socket.setdefaulttimeout(0.00001)

ip = input("Enter IP address to scan: ")

for port in range(1,65536):
    is_port_open(ip, port)