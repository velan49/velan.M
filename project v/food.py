from tkinter import*
from tkinter import ttk
from tkinter import*
from tkinter import messagebox
import login2
from PIL import Image
from PIL.ImageTk import PhotoImage
#global
labelfont=("Garamond",20,"bold")
titlefont=("time new roman",28,"bold")
labelfont=("Garamond",20,"bold")
root=Tk()
root.geometry("1500x700")
titleframe=Frame(root,width=1600,height=70,bg="blue")
titlelabel=Label(titleframe,text="𝓩ØмØ𝐓Ø",bg="blue",fg="red",font=titlefont)
titlelabel.place(relx=0.40,rely=0.3)
titleframe.pack()


mainframe=Frame(root,width=1500,height=600,bg="yellow")
mainframe.place(relx=0.001,rely=0.1)
img1=PhotoImage(Image.open("doot.jpg"))
label=Label(root,image=img1)
label.place(relx=0.00000001,rely=0.1)
def customarpage():
    root.destroy()
    root=Tk()
    root.mainloop()
b=Button(root,text="GO TO BOOK",font=labelfont,bg="sky blue",command=lambda:login2.login())
b.place(relx=0.40,rely=0.38)

bottomframe=Frame(root,width=1600,height=60,bg="blue")
bottomlabel=Label(bottomframe,text="Zomoto.com",bg="blue",fg="red",font=titlefont)
bottomlabel.place(relx=0.34,rely=0.001)
bottomframe.place(relx=0.001,rely=0.95)
root.mainloop()