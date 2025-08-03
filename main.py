
import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(500, 300)

#------label--------

# my_label = tkinter.Label(text="This is Kabir")  #should define text = " " neither its not work
my_label = tkinter.Label(text="This is Kabir", font=("Arial", 18, "bold"))  
my_label.pack()




window.mainloop()

