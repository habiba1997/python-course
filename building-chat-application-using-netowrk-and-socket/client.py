import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = 'localhost'
PORT = 1234
s.connect((HOST_NAME, PORT))
# 100 => buffer size, when sending from server to client
# I need to send data in form of chunks
# I am setting the value or size of chunk I can receive
#  when you decrease the buffer size 10, only part of message will be recieved
while True:
    message = ""
    while True:
        msg = s.recv(5)
        if len(msg) <= 0:
            break
        message += msg.decode('utf-8')
    #  decode the message
    if len(message) > 0:
        print(message)
