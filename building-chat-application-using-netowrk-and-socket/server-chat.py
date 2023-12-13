import socket
# from tkinter import *
#
# root = Tk()
# entry = Entry()
# entry.pack(side=BOTTOM)
# listbox = Listbox(root)
# listbox.pack()
#
# button = Button(root, text="Send")
# button.pack()
# root.mainloop()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = 'localhost'
PORT = 1234

s.bind((HOST_NAME, PORT))
s.listen(4)
client, address = s.accept()

while True:
    message = input('Server: ')
    client.send(bytes(message, 'utf-8'))

    message_from_client = client.recv(50)
    print("Client: ", message_from_client.decode('utf-8'))
