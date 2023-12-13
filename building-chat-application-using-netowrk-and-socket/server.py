import socket

# AF_INET = Address Family Inet = IP4, SOCK_STREAM => STREAM OF DATA
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
#  name of device on local network
print(HOST_NAME)

HOST_NAME = 'localhost'
PORT = 1234

# I am currently connecting the usb cable to send data in into IP and PORT
s.bind((HOST_NAME, PORT))

#  listen connection from client
s.listen(4)

while True:
    client, address = s.accept()
    client.send(bytes("hey there, whatsapp? ", 'utf-8'))
    print("Client is connected and has teh address", address)
    client.close()
