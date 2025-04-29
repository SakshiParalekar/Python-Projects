from tkinter import*


def calculate():
    a=int(Entry.get(e2))
    b=Entry.get(e1)
    age=2024-a
    print(f" %s your age is %s"%(b,age))



root=Tk()
root.title("Age Calculator")


lbl1=Label(root,text="Name")
lbl1.grid(row=0,column=0)

lbl2=Label(root,text="Year")
lbl2.grid(row=1,column=0)

lbl3=Label(root,text="Month")
lbl3.grid(row=2,column=0)

lbl4=Label(root,text="Day")
lbl4.grid(row=3,column=0)


e1=Entry(root)
e1.grid(row=0,column=1)

e2=Entry(root)
e2.grid(row=1,column=1)

e3=Entry(root)
e3.grid(row=2,column=1)

e4=Entry(root)
e4.grid(row=3,column=1)


btn=Button(root,text="Calculate age",bg="black",fg="white",bd=5,command=calculate)
btn.grid(row=4,column=1)



root.mainloop()
