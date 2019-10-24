import socket 

target_host = "192.168.0.12"
target_port = 9999

# instantiate the socket object
# AF_INET paramter says we are going to use a IPV4 address/hostname, SOCK_STREAM indicates it will be a TCP client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the client
client.connect((target_host, target_port))

# transmit data
client.send("hello")

# catch the response
response = client.recv(4096)

print response