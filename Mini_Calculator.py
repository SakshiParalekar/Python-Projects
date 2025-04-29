from tkinter import*


def add():
    a=int(Entry.get(e1))
    b=int(Entry.get(e2))
    addition=a+b
    r3.insert("0",addition)

def sub():
    a=int(Entry.get(e1))
    b=int(Entry.get(e2))
    subtraction=a-b
    r3.insert("0",subtraction)

def mul():
    a=int(Entry.get(e1))
    b=int(Entry.get(e2))
    multiplication=a*b
    r3.insert("0",multiplication)

def div():
    a=int(Entry.get(e1))
    b=int(Entry.get(e2))
    division=a/b
    r3.insert("0",division)

def clear():
    e1.delete("0",END)
    e2.delete("0",END)
    r3.delete("0",END)
    
root=Tk()
root.title("Calculator")


lbl1=Label(root,text="1st No.")
lbl1.grid(row=0,column=0)
lbl2=Label(root,text="2nd No.")
lbl2.grid(row=1,column=0)
lbl3=Label(root,text="Result")
lbl3.grid(row=2,column=0)


e1=Entry(root)
e1.grid(row=0,column=1)
e2=Entry(root)
e2.grid(row=1,column=1)
r3=Entry(root)
r3.grid(row=2,column=1)


btn=Button(root,text="+",command=add)
btn.grid(row=3,column=0)

btn1=Button(root,text="-",command=sub)
btn1.grid(row=3,column=1)

btn2=Button(root,text="*",command=mul)
btn2.grid(row=4,column=0)

btn3=Button(root,text="/",command=div)
btn3.grid(row=4,column=1)

btn4=Button(root,text="Clear",command=clear)
btn4.grid(row=5,column=1)

root.mainloop()
