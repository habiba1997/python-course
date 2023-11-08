from tkinter import *
from tkinter import filedialog
from text_to_speech_converter_module import text_to_speech


def get_text_turn_to_speech():
    text = text_entry.get()
    text_to_speech(text, 'en')


window = Tk()
window.title('text to speech engine')

canvas = Canvas(window, width=400, height=300)
canvas.pack()

text_entry = Entry(window)
canvas.create_window(200, 180, window=text_entry)

button = Button(
    window, text="Start",
    command=lambda: get_text_turn_to_speech()
)
canvas.create_window(200, 230, window=button)

window.mainloop()
