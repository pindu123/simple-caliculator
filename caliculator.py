import tkinter
from tkinter import *
cal=Tk()
cal.title("Simple calculator")
cal.geometry("570x600+100+200")
cal.resizable(False,False) 
cal.configure(bg="black")


equation=""

def show(value):
    global equation
    equation+=value
    calresult.config(text=equation)

def clear():
    global equation
    equation=""
    calresult.config(text=equation)
def caliculate():
    global equation
    result=""
    if equation != "":
        try:
            result=eval(equation)
        except:
            result="error"
            equation=""
    calresult.config(text=result)


calresult=Label(cal,width=25,height=2,text="",font=("arial",30))
calresult.pack()

Button(cal,text="1",width=6,height=2,font=("arial",30,"bold"),bd=1,fg="#e0d0ce",bg="grey",command=lambda:show("1")).place(x=10,y=100)
Button(cal,text="2",width=6,height=2,font=("arial",30,"bold"),bd=1,fg="#e0d0ce",bg="grey",command=lambda:show("2")).place(x=150,y=100)
Button(cal,text="3",width=6,height=2,font=("arial",30,"bold"),bd=1,fg="#e0d0ce",bg="grey",command=lambda:show("3")).place(x=290,y=100)
Button(cal,text="*",width=6,height=2,font=("arial",30,"bold"),bd=1,fg="#e0d0ce",bg="grey",command=lambda:show("*")).place(x=430,y=100)

Button(cal,text="4",width=6,height=2,font=("arial",30,"bold"),bd=1,fg="#e0d0ce",bg="grey",command=lambda:show("4")).place(x=10,y=200)
Button(cal,text="5",width=6,height=2,font=("arial",30,"bold"),bd=1,fg="#e0d0ce",bg="grey",command=lambda:show("5")).place(x=150,y=200)
Button(cal,text="6",width=6,height=2,font=("arial",30,"bold"),bd=1,fg="#e0d0ce",bg="grey",command=lambda:show("6")).place(x=290,y=200)
Button(cal,text="+",width=6,height=2,font=("arial",30,"bold"),bd=1,fg="#e0d0ce",bg="grey",command=lambda:show("-")).place(x=430,y=200)

Button(cal,text="7",width=6,height=2,font=("arial",30,"bold"),bd=1,fg="#e0d0ce",bg="grey",command=lambda:show("7")).place(x=10,y=300)
Button(cal,text="8",width=6,height=2,font=("arial",30,"bold"),bd=1,fg="#e0d0ce",bg="grey",command=lambda:show("8")).place(x=150,y=300)
Button(cal,text="9",width=6,height=2,font=("arial",30,"bold"),bd=1,fg="#e0d0ce",bg="grey",command=lambda:show("9")).place(x=290,y=300)
Button(cal,text="-",width=6,height=2,font=("arial",30,"bold"),bd=1,fg="#e0d0ce",bg="grey",command=lambda:show("+")).place(x=430,y=300)

Button(cal,text="0",width=6,height=2,font=("arial",30,"bold"),bd=1,fg="#e0d0ce",bg="grey",command=lambda:show("0")).place(x=10,y=400)
Button(cal,text="/",width=6,height=2,font=("arial",30,"bold"),bd=1,fg="#e0d0ce",bg="grey",command=lambda:show("/")).place(x=150,y=400)
Button(cal,text="%",width=6,height=2,font=("arial",30,"bold"),bd=1,fg="#e0d0ce",bg="grey",command=lambda:show("%")).place(x=290,y=400)
Button(cal,text="c",width=6,height=2,font=("arial",30,"bold"),bd=1,fg="#e0d0ce",bg="grey",command=lambda:clear()).place(x=430,y=400)

Button(cal,text=".",width=6,height=2,font=("arial",30,"bold"),bd=1,fg="#e0d0ce",bg="grey",command=lambda:show(".")).place(x=10,y=500)
Button(cal,text="(",width=6,height=2,font=("arial",30,"bold"),bd=1,fg="#e0d0ce",bg="grey",command=lambda:show("(")).place(x=150,y=500)
Button(cal,text=")",width=6,height=2,font=("arial",30,"bold"),bd=1,fg="#e0d0ce",bg="grey",command=lambda:show(")")).place(x=290,y=500)
Button(cal,text="=",width=6,height=2,font=("arial",30,"bold"),bd=1,fg="#e0d0ce",bg="grey",command=lambda:caliculate()).place(x=430,y=500)

cal.mainloop()
