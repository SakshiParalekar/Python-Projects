from tkinter import*

def clear():
    e1.delete("0",END)
    e2.delete("0",END)
    e3.delete("0",END)
    si.delete("0",END)
    fa.delete("0",END)
    

def calculate():
    a=float(Entry.get(e1))
    b=float(Entry.get(e2))
    c=float(Entry.get(e3))
    Simple_Interest=(a*b*c)/100
    si.insert("0",Simple_Interest)
    final=Simple_Interest+a
    fa.insert("0",final)


root=Tk()
root.title("Basic Simple Interest Calculator")

lbl1=Label(root,text="Principal")
lbl1.grid(row=0,column=0)

lbl2=Label(root,text="Rate")
lbl2.grid(row=1,column=0)

lbl2=Label(root,text="Time")
lbl2.grid(row=2,column=0)

lbl3=Label(root,text="Simple Interest")
lbl3.grid(row=4,column=0)

lbl4=Label(root,text="Final Amount")
lbl4.grid(row=5,column=0)

e1=Entry(root)
e1.grid(row=0,column=1)
e2=Entry(root)
e2.grid(row=1,column=1)
e3=Entry(root)
e3.grid(row=2,column=1)
si=Entry(root)
si.grid(row=4,column=1)
fa=Entry(root)
fa.grid(row=5,column=1)

btn1=Button(root,text="Calculate",command=calculate)
btn1.grid(row=3,column=1)
btn2=Button(root,text="Clear",command=clear)
btn2.grid(row=3,column=2)



root.mainloop()

