
from tkinter import *

window = Tk()
window.title("Widgets Examples")
window.minsize(500, 500)

# ---Labels-----
label = Label(text="this is old text")
# config will update the old text vallue in the screen---
label.config(text="This is new text")
label.pack()

# ------buttons------
def action():
    print("do something")

btn = Button(text="Click Me", command=action)
btn.pack()

# --------Entries -----
entry = Entry(width=40)
entry.insert(END, string="some text to begin with")
print(entry.get())
entry.pack()

# -----text-------

txt = Text(width=30, height=5)
txt.focus()
txt.insert(END, "Examples of multiline text field")
print(txt.get("1.0", END))
txt.pack()

# ------spinbox-----
def spin_used():
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spin_used)
spinbox.pack()

# --------scale--------
def scale_used(value):
    print(value)

scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# -----check button -------
def chk_used():
    print(chk_state.get())

chk_state = IntVar()
chkbtn = Checkbutton(text="is on", variable=chk_state, command=chk_used)
chk_state.get()
chkbtn.pack()

# ------radio button--------
def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radiobtn1 = Radiobutton(text="option-1", value=1, variable=radio_state, command=radio_used)
radiobtn2 = Radiobutton(text="option-2", value=2, variable=radio_state, command=radio_used)
radio_state.get()
radiobtn1.pack()
radiobtn2.pack()

# -----List box -----
def lstbox_used(event):
    print(lstbox.get(lstbox.curselection()))

lstbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    lstbox.insert(fruits.index(item), item)
lstbox.bind("<<ListboxSelect>>", lstbox_used)
lstbox.pack()


window.mainloop()
