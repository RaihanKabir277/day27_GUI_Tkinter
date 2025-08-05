
from tkinter import *

Window = Tk()
Window.title("My first GUI program")
Window.minsize(500, 300)
# ------ add padding -------
Window.config(padx=20, pady=20)  #for all window screen

# --label---

my_label = Label(text="Iam a label", font=("Arial", 24, "bold"))
my_label.config(text="New text")
# my_label.pack(side="left")   #in this function we could not set the label in a random place as user want
# my_label.place(x=0, y=0)    #suppose we have 100 widgets so we have to be defined 100 times place() thats why grid is come to solve this
# my_label.place(x=100, y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)  #padding just for label 

# ---button----
def button_clicked():
    pass
def btn1_clicked():
    pass

btn = Button(text="click me", command=button_clicked)
# btn.pack(side="left")
btn.grid(column=1, row=1)

btn1 = Button(text="BTN2", command=btn1_clicked)
btn1.grid(column=2, row=0)

#------ entery----

input = Entry(width=10)
print(input.get())
# input.pack(side="left")
input.grid(column=3, row=2)

Window.mainloop()
