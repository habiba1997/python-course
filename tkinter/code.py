# Lecture: Hello


from tkinter import *

root = Tk()
hello = Label(root, text="hello world")

hello.pack()

root.mainloop()

root.geometry("300x400")


# Lecture: Understanding
# Tkinter
# widgets.
#
# hello = Label(root, text="hello world", font=("Arial", 16), fg="red", bg="white")
#
# Lecture: Button
# widget
# button = Button(root, text="Click here")
# button.pack()
#
# button = Button(root, text="Click here", command=display)
#
#
# def display():
#     print('This is a display message')
#
#
# Lecture: Accepting
# user
# Input
#
# from tkinter import *
#
#
# def display():
#     print(entry.get())
#
#
# root = Tk()
# hello = Label(root, text="Enter some text")
# hello.pack()
#
# entry = Entry(root)
# entry.pack()
# button = Button(root, text="Click here", command=display)
# button.pack()
#
# root.geometry("300x400")
# root.mainloop()
#
# Lecture: Adding
# two
# numbers
# from tkinter import *
#
#
# def add():
#     n1 = int(number1.get())
#     n2 = int(number2.get())
#     print(n1 + n2)
#
#
# root = Tk()
# hello = Label(root, text="Enter some text")
# hello.pack()
#
# number1 = Entry(root)
# number1.pack()
#
# number2 = Entry(root)
# number2.pack()
# button = Button(root, text="Click here", command=add)
# button.pack()
#
# root.geometry("300x400")
# root.mainloop()
#
# from tkinter import *
#
#
# def add():
#     n1 = int(number1.get())
#     n2 = int(number2.get())
#
#     result = str(n1 + n2)
#     answer.config(text="Answer is: " + result)
#
#
# root = Tk()
# hello = Label(root, text="Enter some text")
# hello.pack()
#
# number1 = Entry(root)
# number1.pack()
#
# number2 = Entry(root)
# number2.pack()
# button = Button(root, text="Click here", command=add)
# button.pack()
#
# answer = Label(root)
# answer.pack()
#
# root.geometry("300x400")
# root.mainloop()
#
# Lecture: Checkboxes
#
# from tkinter import *
#
#
# def selected():
#     label.config(text=var.get())
#
#
# root = Tk()
#
# var = BooleanVar()
# checkbox = Checkbutton(root, text="Accept terms", variable=var, command=selected)
# checkbox.pack()
#
# label = Label(root)
# label.pack()
# root.geometry("300x400")
# root.mainloop()
#
# from tkinter import *
#
#
# def selected():
#     sugar = sugar_var.get()
#     ice = ice_var.get()
#     cream = cream_var.get()
#     if sugar:
#         sugar = "sugar"
#     else:
#         sugar = "no sugar"
#
#     if ice:
#         ice = "ice"
#     else:
#         ice = "no ice"
#
#     if cream:
#         cream = "cream"
#     else:
#         cream = "no cream"
#
#     print(sugar)
#     label.config(text="Options selected are: " + "\\n" + sugar + "\\n" + ice + "\\n" + cream)
#
#
# root = Tk()
#
# sugar_var = BooleanVar()
# ice_var = BooleanVar()
# cream_var = BooleanVar()
#
# sugar_checkbox = Checkbutton(root, text="Sugar", variable=sugar_var, command=selected)
# sugar_checkbox.pack()
#
# ice_checkbox = Checkbutton(root, text="Ice", variable=ice_var, command=selected)
# ice_checkbox.pack()
#
# cream_checkbox = Checkbutton(root, text="Cream", variable=cream_var, command=selected)
# cream_checkbox.pack()
#
# label = Label(root)
# label.pack()
# root.geometry("300x400")
# root.mainloop()
#


# Lecture: Radiobuttons
#
# from tkinter import *
#
#
# def selected():
#     label.config(text="Choice of fuel is: " + fuel.get())
#
#
# root = Tk()
# # Create a variable to store radiobutton state
# fuel = StringVar(value="Petrol")
#
# radio1 = Radiobutton(root, text="Petrol", value="Petrol", variable=fuel, command=selected)
# radio2 = Radiobutton(root, text="Diesel", value="Diesel", variable=fuel, command=selected)
# radio3 = Radiobutton(root, text="Electric", value="Electric", variable=fuel, command=selected)
#
# label = Label(root)
# label.pack()
# radio1.pack()
# radio2.pack()
# radio3.pack()
# root.geometry("300x400")
# root.mainloop()
#
# Lecture: Frames
#
# from tkinter import *
#
# root = Tk()
#
# root.geometry("300x400")
# root.mainloop()
# from tkinter import *
#
# root = Tk()
#
# # create a frame object
# frame = Frame(root)
# frame.pack()
#
# # now let's create another frame
# frame2 = Frame(root)
# frame2.pack()
#
# # now let's create some widgets and add them to a frame
# # instead of adding it to the root window, we will pass frame here
# button1 = Button(frame, text="Button1")
# button2 = Button(frame2, text="button2")
#
# # we still need to pack these buttons
# button1.pack()
# button2.pack()
#
# root.geometry("300x400")
# root.mainloop()
#
# frame2.pack(side=BOTTOM)
#
# Lecture: Grid
# layout
# manager
#
# from tkinter import *
#
# root = Tk()
#
# label1 = Label(root, text='Email')
# label2 = Label(root, text="Password")
#
# text1 = Entry(root)
# text2 = Entry(root)
#
# label1.grid(row=0, column=0)
# label2.grid(row=1, column=0)
#
# text1.grid(row=0, column=1)
# text2.grid(row=1, column=1)
#
# button = Button(root, text='Login')
# button.grid(row=2, column=1)
# root.geometry("300x400")
# root.mainloop()
#
# Lecture: Using
# grid
# layout
# manager
# with frames.
#
# from tkinter import *
#
# root = Tk()
#
# for x in range(3):
#     for y in range(3):
#         frame = Frame(root)
#
#         frame.grid(row=x, column=y)
#
#         button = Button(frame, text=f"Row{x} \\n Column{y}")
#
#         button.pack()
#
# root.mainloop()
#
# button.pack(padx=5, pady=5)
#
# Lecture: Writing
# Tkinter
# code
# the
# OOP
# way.
#
# from tkinter import *
#
#
# class Demo:
#
#     def __init__(self, rootone):
#         frame = Frame(rootone)
#         frame.pack()
#         # as this is a class instead of saying printbutton we use self
#
#         self.printbutton = Button(frame, text='Click Here', command=self.printmessage)
#         self.printbutton.pack()
#
#         self.quitbutton = Button(frame, text='Exit', command=frame.quit)
#         self.quitbutton.pack()
#
#     def printmessage(self):
#         print("Button Clicked!")
#
#
# root = Tk()
#
# b = Demo(root)
#
# root.mainloop()
#
# Lecture: Drop
# down
# menus
#
# from tkinter import *
#
#
# def function1():
#     print('Menu item clicked')
#
#
# root = Tk()
#
# mymenu = Menu(root)
#
# root.config(menu=mymenu)
#
# submenu = Menu(mymenu)
#
# mymenu.add_cascade(label="File", menu=submenu)
#
# submenu.add_command(label="Project", command=function1)
#
# submenu.add_command(label="Save", command=function1)
#
# root.mainloop()
#
# Lecture: Adding
# statusbar
#
# status = Label(root, text="This is the status", bd=1, relief=SUNKEN, anchor=W)
# status.pack(side=BOTTOM, fill=X)
#
# Lecture: Toolbar
# toolbar = Frame(root, bg='green')
# insertbutton = Button(toolbar, text='Insert Files', command=function1)
# insertbutton.pack(side=LEFT, padx=2, pady=3)
#
# printbutton = Button(toolbar, text='Print ', command=function1)
# printbutton.pack(side=LEFT, padx=2, pady=3)
#
# Lecture
# 17: Messagebox
#
# import tkinter.messagebox
# from tkinter import *
#
# root = Tk()
#
# tkinter.messagebox.showinfo("Title", "This is a messagebox")
# # ask question inside a messagebox
# response = tkinter.messagebox.askquestion("Question1", "Do you like coffee")
# if response == "yes":
#     print('Here is a coffee for you')
# root.mainloop()