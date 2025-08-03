
import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(500, 300)

#------label--------

# my_label = tkinter.Label(text="This is Kabir")  #should define text = " " neither its not work
my_label = tkinter.Label(text="This is Kabir", font=("Arial", 18, "bold"))  
my_label.pack(side="bottom", expand=1)
# my_label.pack()

# --------Argument with default values----------

# def fun(a=1, b=2, c=3):
#     a = b
#     b= c
#     print(a)

# fun()   #no need to give argument by default it will work perfectly 
# fun(b=5)   #it will work also 




window.mainloop()

