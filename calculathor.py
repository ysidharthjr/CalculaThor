#!/usr/bin/env python3
from tkinter import *
from tkinter import messagebox
import math

root=Tk()

for x in range(5):
    Grid.rowconfigure(root, x, weight=1)
for y in range(7):
    Grid.columnconfigure(root, y, weight=1)

root.title("Calcula-Thor")
l1=Label(root,text="Calcula-Thor",fg="green")
l1.config(font=("Courier", 15))
l1.grid(row=6,columnspan=7,sticky=N+S+E+W)
l1=Label(root,text="By: Yashashwi Sidharth",fg="red")
l1.grid(row=7,columnspan=7,sticky=N+S+E+W)

f1=Entry(root,bg="lightyellow")
f1.grid(row=0,columnspan=6,sticky=N+S+E+W)

def calcu():
    eq=f1.get()
    f1.delete(0,END)
    try:
        F = eval(eq)
        f1.insert(0,F)
    except:
        messagebox.showerror("Seriously?", "I am Calcula-Thor son of Py-Din and you caused an error !")

b1=Button(root,text="1",command=lambda:f1.insert(END,"1"),bg="yellow")
b1.grid(row=1,column=0,sticky=N+S+E+W)
b1=Button(root,text="2",command=lambda:f1.insert(END,"2"),bg="yellow")
b1.grid(row=1,column=1,sticky=N+S+E+W)
b1=Button(root,text="3",command=lambda:f1.insert(END,"3"),bg="yellow")
b1.grid(row=1,column=2,sticky=N+S+E+W)
b1=Button(root,text="4",command=lambda:f1.insert(END,"4"),bg="yellow")
b1.grid(row=2,column=0,sticky=N+S+E+W)
b1=Button(root,text="5",command=lambda:f1.insert(END,"5"),bg="yellow")
b1.grid(row=2,column=1,sticky=N+S+E+W)
b1=Button(root,text="6",command=lambda:f1.insert(END,"6"),bg="yellow")
b1.grid(row=2,column=2,sticky=N+S+E+W)
b1=Button(root,text="7",command=lambda:f1.insert(END,"7"),bg="yellow")
b1.grid(row=3,column=0,sticky=N+S+E+W)
b1=Button(root,text="8",command=lambda:f1.insert(END,"8"),bg="yellow")
b1.grid(row=3,column=1,sticky=N+S+E+W)
b1=Button(root,text="9",command=lambda:f1.insert(END,"9"),bg="yellow")
b1.grid(row=3,column=2,sticky=N+S+E+W)
b1=Button(root,text=".",command=lambda:f1.insert(END,"."),bg="cyan")
b1.grid(row=4,column=0,sticky=N+S+E+W)
b1=Button(root,text="0",command=lambda:f1.insert(END,"0"),bg="yellow")
b1.grid(row=4,column=1,sticky=N+S+E+W)
b1=Button(root,text="=",command=calcu,bg="lime")
b1.grid(row=4,column=2,sticky=N+S+E+W)
b1=Button(root,text="+",command=lambda:f1.insert(END,"+"),bg="lightblue")
b1.grid(row=1,column=3,sticky=N+S+E+W)
b1=Button(root,text="-",command=lambda:f1.insert(END,"-"),bg="lightblue")
b1.grid(row=2,column=3,sticky=N+S+E+W)
b1=Button(root,text="*",command=lambda:f1.insert(END,"*"),bg="lightblue")
b1.grid(row=3,column=3,sticky=N+S+E+W)
b1=Button(root,text="/",command=lambda:f1.insert(END,"/"),bg="lightblue")
b1.grid(row=4,column=3,sticky=N+S+E+W)
b1=Button(root,text="(",command=lambda:f1.insert(END,"("),bg="blue")
b1.grid(row=1,column=4,sticky=N+S+E+W)
b1=Button(root,text=")",command=lambda:f1.insert(END,")"),bg="blue")
b1.grid(row=1,column=5,sticky=N+S+E+W)
b1=Button(root,text="^",command=lambda:f1.insert(END,"**"),bg="lightgreen")
b1.grid(row=2,column=4,sticky=N+S+E+W)
b1=Button(root,text="%",command=lambda:f1.insert(END,"%"),bg="lightgreen")
b1.grid(row=3,column=4,sticky=N+S+E+W)

def sqroot():
    eq=f1.get()
    f1.delete(0,END)
    try:
        F = math.sqrt(eval(eq))
        f1.insert(0,F)
    except:
        messagebox.showerror("Seriously?", "I am Calcula-Thor son of Py-Din and you caused an error !")

def logg():
    eq=f1.get()
    f1.delete(0,END)
    try:
        F = math.log10(eval(eq))
        f1.insert(0,F)
    except:
        messagebox.showerror("Seriously?", "I am Calcula-Thor son of Py-Din and you caused an error !")

b1=Button(root,text="Sqrt",command=sqroot,bg="lightgreen")
b1.grid(row=4,column=4,sticky=N+S+E+W)
b1=Button(root,text="log",command=logg,bg="lightgreen")
b1.grid(row=2,column=5,sticky=N+S+E+W)
b1=Button(root,text="pi",command=lambda:f1.insert(END,math.pi),bg="lightgreen")
b1.grid(row=3,column=5,sticky=N+S+E+W)
b1=Button(root,text="e",command=lambda:f1.insert(END,math.e),bg="lightgreen")
b1.grid(row=4,column=5,sticky=N+S+E+W)

def logn():
    eq=f1.get()
    f1.delete(0,END)
    try:
        F = math.log(eval(eq))
        f1.insert(0,F)
    except:
        messagebox.showerror("Seriously?", "I am Calcula-Thor son of Py-Din and you caused an error !")

def sine():
    eq=f1.get()
    f1.delete(0,END)
    try:
        F = math.sin(eval(eq))
        f1.insert(0,F)
    except:
        messagebox.showerror("Seriously?", "I am Calcula-Thor son of Py-Din and you caused an error !")

def cosine():
    eq=f1.get()
    f1.delete(0,END)
    try:
        F = math.cos(eval(eq))
        f1.insert(0,F)
    except:
        messagebox.showerror("Seriously?", "I am Calcula-Thor son of Py-Din and you caused an error !")

def tangent():
    eq=f1.get()
    f1.delete(0,END)
    try:
        F = math.tan(eval(eq))
        f1.insert(0,F)
    except:
        messagebox.showerror("Seriously?", "I am Calcula-Thor son of Py-Din and you caused an error !")


b1=Button(root,text="ln",command=logn,bg="lightgreen")
b1.grid(row=1,column=6,sticky=N+S+E+W)
b1=Button(root,text="sin",command=sine,bg="magenta")
b1.grid(row=2,column=6,sticky=N+S+E+W)
b1=Button(root,text="cos",command=cosine,bg="magenta")
b1.grid(row=3,column=6,sticky=N+S+E+W)
b1=Button(root,text="tan",command=tangent,bg="magenta")
b1.grid(row=4,column=6,sticky=N+S+E+W)

b1=Button(root,text="C",command=lambda:f1.delete(0,END),bg="red")
b1.grid(row=0,column=6,sticky=N+S+E+W)

root.mainloop()
