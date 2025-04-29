from tkinter import*

root=Tk()
root.title("Font,Size and color")

def render():
    t.config(font=(var1.get(),var2.get()),fg=var3.get())
t=Text(root,height=5,bd=5)
t.grid(row=0,column=1)


lbl1=Label(root,text="Enter text")
lbl1.grid(row=0,column=0)
lbl2=Label(root,text="Font")
lbl2.grid(row=1,column=0)
lbl3=Label(root,text="Size")
lbl3.grid(row=1,column=1)
lbl4=Label(root,text="Color")
lbl4.grid(row=1,column=2)


var1=StringVar()
rd1=Radiobutton(root,text="Arial",variable=var1,value="Arial")
rd1.grid(row=2,column=0)
rd2=Radiobutton(root,text="Times New Roman",variable=var1,value="Times New Roman")
rd2.grid(row=3,column=0)
rd3=Radiobutton(root,text="Comicsansms",variable=var1,value="Comicsansms")
rd3.grid(row=4,column=0)

var2=IntVar()
rd4=Radiobutton(root,text="8",variable=var2,value="8")
rd4.grid(row=2,column=1)
rd5=Radiobutton(root,text="10",variable=var2,value="10")
rd5.grid(row=3,column=1)
rd6=Radiobutton(root,text="12",variable=var2,value="12")
rd6.grid(row=4,column=1)

var3=StringVar()
rd7=Radiobutton(root,text="Red",variable=var3,value="Red")
rd7.grid(row=2,column=2)
rd8=Radiobutton(root,text="Blue",variable=var3,value="Blue")
rd8.grid(row=3,column=2)
rd9=Radiobutton(root,text="Yellow",variable=var3,value="Yellow")
rd9.grid(row=4,column=2)

btn=Button(root,text="Render",command=render)
btn.grid(row=5,column=0)

root.mainloop()
