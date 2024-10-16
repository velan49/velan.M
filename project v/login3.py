from tkinter import *
from tkinter import ttk

def book():
    titlefont=("time new roman",28,"bold")
    labelfonts=("Garamond",20,"bold")
    labelfont=("Garamond",15,"bold")
    root=Tk()
    root.geometry("1500x700")
    mainframe=Frame(root,width=1500,height=800,bg="red")
    mainframe.place(relx=0.01,rely=0.001)
    miniframe=Frame(mainframe,width=1500,height=400,bg="gold")
    miniframe.place(relx=0.001,rely=0.2)
    titlelabel=Label(mainframe,text="ZOMOTO",bg="red",font=titlefont)
    
    titlelabel.place(relx=0.39,rely=0.01)


    combo = ttk.Combobox(miniframe, values=["BIRIYANI","CAKE","JUICE","SWEET"],font=labelfont)
    combo.place(relx=0.40,rely=0.34)
    combo1 = ttk.Combobox(miniframe)
    combo1.place(relx=0.40,rely=0.47)
    #combo2 = ttk.Combobox(miniframe,values=["1A","2A","3B","4D","5E"])
    #combo2 = ttk.Combobox(miniframe,values=["6A","7d","8S","6W"])
    #combo2 = ttk.Combobox(miniframe,values=["","","",""])
    #combo2.place(relx=0.40,rely=0.59)
    def movies(event):
        movies=combo.get()
        if(movies=="BIRIYANI"):
            combo1.config(values=["CHICKEN BIRIYANI","MUTTON BIRIYANI"],font=labelfont)
        elif(movies=="CAKE"):
            combo1.config(values=["BLACKFORST","WHITEFOREST","REDVELVET"],font=labelfont)
        if(movies=="JUICE"):
            combo1.config(values=["APPLE","ORANGE","LEMON"],font=labelfont)
        elif(movies=="SWEET"):
            combo1.config(values=["RASAGULA","LADDU","GULAJAMUN"],font=labelfont)
    '''
def boc(event):
    boc=combo1.get()
    if(boc=="VIRAT BOC"):
        combo2.config(values=["1A","2A","3B","4D","5E"])
    elif(boc=="ABD BOC"):
        combo2.config(values=["6A","7d","8S","6W"])
    elif(boc=="GYLE BOC"):
        combo2.config(values=["22A","71d","82S","61W"])
'''        
    combo.bind("<<ComboboxSelected>>",movies)  
    #combo = ttk.Combobox(miniframe, values=["VIRAT BOC","ABD BOC","GYLE BOC"],font=labelfont)

    alabel=Label(miniframe,text="WELCOME TO FOOD WORLD",font=labelfonts,bg="sky blue").place(relx=0.30,rely=0.10)
    alabel=Label(miniframe,text="FOODS:",font=labelfonts,bg="pink").place(relx=0.2,rely=0.35)
    alabel=Label(miniframe,text="FOOD NAME:",font=labelfonts,bg="pink").place(relx=0.2,rely=0.47)
    alabel=Label(miniframe,text="QUANTITY :",font=labelfonts,bg="pink").place(relx=0.2,rely=0.59)
    centry=Entry(mainframe,font=labelfont)
    centry.place(relx=0.4,rely=0.50)
    alabel=Label(miniframe,text="ADDRESS:",font=labelfonts,bg="pink").place(relx=0.2,rely=0.71)
    centry=Entry(mainframe,font=labelfont)
    centry.place(relx=0.4,rely=0.57)
    b=Button(root,text="ORDER",font=labelfont,bg="white")
    b.place(relx=0.45,rely=0.8)
    #bentry=Entry(miniframe,font=labelfonts)
    #bentry.place(relx=0.40,rely=0.34)
    #bentry=Entry(miniframe,font=labelfonts)
    #bentry.place(relx=0.40,rely=0.47)
    #bentry=Entry(miniframe,font=labelfonts)
    #bentry.place(relx=0.40,rely=0.59)

    labelfont=("Garamond",15,"bold")





    root.mainloop()