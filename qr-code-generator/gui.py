from tkinter import *
from generator_module import *
import tkinter.messagebox
from PIL import ImageTk, Image
import png


def generate(name, link):
    filename = name + ".png"
    # qr code from link
    url = pyqrcode.create(link)
    url.png(file=filename, scale=8)
    # created an image.open from filename, and created a photo image from it to add it to label
    image = ImageTk.PhotoImage(Image.open(filename))
    image_label = Label(image=image)
    image_label.image = image
    canvas.create_window(200, 450, window=image_label)


window = Tk()
window.title('text to speech engine')

canvas = Canvas(window, width=400, height=700)
canvas.pack()

app_label = Label(window, text="QR Code Generator", fg='blue', font=("Arial", 30))
canvas.create_window(200, 50, window=app_label)

name_label = Label(window, text="Link name")
link_label = Label(window, text="Link")
canvas.create_window(200, 100, window=name_label)
canvas.create_window(200, 160, window=link_label)

name_entry = Entry(window)
link_entry = Entry(window)
canvas.create_window(200, 130, window=name_entry)
canvas.create_window(200, 180, window=link_entry)

button = Button(
    window, text="Generate QR Code",
    command=lambda: generate(
        name_entry.get(),
        link_entry.get()
    )
)
canvas.create_window(200, 210, window=button)


window.mainloop()
