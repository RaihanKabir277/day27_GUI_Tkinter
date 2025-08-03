
import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(500, 300)

#------label--------

# my_label = tkinter.Label(text="This is Kabir")  #should define text = " " neither its not work
my_label = tkinter.Label(text="this is kabir", font=("Arial", 18, "bold"))  
# my_label.pack(side="bottom", expand=1)
my_label.pack()
# ------ if we want to change the label value is given below----

# my_label["text"] = "this is raihan"
# my_label.config(text="this is raihan")

def button_clicked():
    print("I got clicked")
    new_text = entry.get()
    my_label.config(text=new_text)

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

# ---------Entry------

entry = tkinter.Entry(width=10)
entry.pack()


# --------Argument with default values----------

# def fun(a=1, b=2, c=3):
#     a = b
#     b= c
#     print(a)

# fun()   #no need to give argument by default it will work perfectly 
# fun(b=5)   #it will work also 

# ---------- from tkinter import * 
# window = tkinter.Tk() instead of this we will write window = Tk()


window.mainloop()

