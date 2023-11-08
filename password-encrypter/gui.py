from tkinter import *
import hashing_module
import tkinter.messagebox

hashed_password = hashing_module.hash_password("1234")


def validate(entered_password):
    if(hashing_module.check_password(entered_password, hashed_password)):
        tkinter.messagebox.showinfo("Success", "Login Successful")
    else:
        tkinter.messagebox.showerror("Failed", "Invalid Password")


root = Tk()
root.title('password validation')
root.geometry("300x300")

password_entry = Entry(root)
password_entry.pack()

button = Button(
    root, text="Validate",
    command=lambda: validate(
        password_entry.get()
    )
)
button.pack()

root.mainloop()
