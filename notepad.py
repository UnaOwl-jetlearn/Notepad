from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *

window = Tk()

window.geometry("900x650")
window.title("Notepad")
window.config(background="lightgreen")


title = Label(window,text="Notepad",font=("arial",35),bg="lightgreen")
title.place(x=350,y=30),

enter_text = Label(window,text="Enter any text in the box below:",bg="lightgreen",font=("arial",15))
enter_text.place(x=150,y=150)

input_text = Entry(window,width=40,font=("arial",15))
input_text.place(x=150,y=180)

textbox = Listbox(window,width=70,height=18,font=("arial",10))
textbox.place(x=150,y=300)


def add_text():
   added_text = input_text.get()
   textbox.insert(END,added_text)
   input_text.delete(0,END)
   messagebox.showinfo("Text Added","Your Text Has Been Added")


def delete_text(): # curselection = current selection
   selected_value = textbox.curselection()
   for i in selected_value:
      textbox.delete(i)

def save_text():
   save_file = asksaveasfile()
   for i in textbox.get(0,END):
      print(i,file=save_file)
      textbox.delete(0,END)

def open_text():
   open_file = askopenfile()
   textbox.delete(0,END)
   items = open_file.readlines()
   for i in items:
    textbox.insert(END,i)


add_button = Button(window,text="Add",font=("arial",15),command=add_text)
add_button.place(x=150,y=230)

delete_button = Button(window,text="Delete",font=("arial",15),command=delete_text)
delete_button.place(x=230,y=230)

save_button = Button(window,text="Save",font=("arial",15),command=save_text)
save_button.place(x=330,y=230)

open_button = Button(window,text="Open",font=("arial",15),command=open_text)
open_button.place(x=420,y=230)


window.mainloop()