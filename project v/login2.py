from tkinter import *
from tkinter import ttk
import login3
from tkinter import messagebox
def login():
    titlefont=("time new roman",28,"bold")
    labelfonts=("Garamond",10,"bold")
    labelfont=("Garamond",15,"bold")
    root=Tk()
    root.geometry("800x400")
    titlelabel=Label(root,text="LOGIN",fg="red",font=titlefont)
    titlelabel.place(relx=0.45,rely=0.01)
    

    ''''
    import re

    # Click on Edit and place your email ID to validate
    email = "my.ownsite@our-earth.org"
    valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
    '''


    alabel=Label(root,text="Enter your name:",fg="black",font=labelfont).place(relx=0.23,rely=0.2)
    aentry=Entry(root,font=labelfonts)
    aentry.place(relx=0.43,rely=0.2)
    email=Label(root,text="Gmail ID:",fg="black",font=labelfont).place(relx=0.23,rely=0.32)
    bentry=Entry(root,font=labelfonts)
    bentry.place(relx=0.43,rely=0.32)
    clabel=Label(root,text="password:",fg="black",font=labelfont).place(relx=0.23,rely=0.45)
    centry=Entry(root,font=labelfonts)
    centry.place(relx=0.43,rely=0.45)
    def log():
        if bentry.get() == "thala07@gmail.com" and centry.get() == "leodas":
            messagebox.showinfo("Login Successful", "Welcome, Admin!")
            login3.book()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

   

    labelfont=("Garamond",15,"bold")
  

  
    b=Button(root,text="DONE",font=labelfont,bg="sky blue",command=lambda:log())
    b.place(relx=0.50,rely=0.55)

    root.mainloop()
