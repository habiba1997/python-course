from tkinter import *
from tkinter import filedialog
from compress_module import compress, decompress

def open_file():
    filename = filedialog.askopenfilename(initialdir='/', title='Select a file to compress')
    return filename

window = Tk()
window.title('compression engine')
window.geometry("600x400")


compress_button = Button(
    window, text="Compress",
    command=lambda: compress(
        open_file(),
        'compress.txt',
    )
)
compress_button.grid(row=4, column=1)
decompress_button = Button(
    window, text="Decompress",
    command=lambda: decompress(
        open_file(),
        'decompress.txt'
    )
)
decompress_button.grid(row=4, column=2)

# compress_input_label = Label(window, text="File path to be compressed")
# compress_input_entry = Entry(window)
# compress_input_label.grid(row=1, column=0)
# compress_input_entry.grid(row=1, column=1, columnspan=2)
#
# compress_output_label = Label(window, text="Name of compressed File")
# compress_output_entry = Entry(window)
# compress_output_label.grid(row=2, column=0)
# compress_output_entry.grid(row=2, column=1, columnspan=2)
#
# decompress_output_label = Label(window, text="Name of decompressed File")
# decompress_output_entry = Entry(window)
# decompress_output_label.grid(row=3, column=0)
# decompress_output_entry.grid(row=3, column=1, columnspan=2)
window.mainloop()