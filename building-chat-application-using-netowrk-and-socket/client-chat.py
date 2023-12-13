import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = 'localhost'
PORT = 1234
s.connect((HOST_NAME, PORT))

while True:
    message = s.recv(50)
    print("Server: ", message.decode('utf-8'))

    message_to_send = input("Client: ")
    s.send(bytes(message_to_send, "utf-8"))
