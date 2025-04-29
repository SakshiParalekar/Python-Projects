from tkinter import*
from tkinter import messagebox

    
root=Tk()
root.title("General Knowledge QUIZ")

root.geometry("600x500")

def openNewWindow1():
    page2 = Toplevel(root)
    page2.title("Page 2")
    page2.geometry("600x500")
    
    lbl2=Label(page2,text="Q2.Smallest state of india ?",font="Helvetica 15 bold")
    lbl2.grid(row=2,column=0)
    var2=StringVar()
    rd1=Radiobutton(page2,text="Goa",variable=var2,value="Maharashtra",font="Helvetica 15 bold")
    rd1.grid(row=3,column=0)
    rd2=Radiobutton(page2,text="Maharashtra",variable=var2,value="Goa",font="Helvetica 15 bold")
    rd2.grid(row=4,column=0)
    rd3=Radiobutton(page2,text="Karnataka",variable=var2,value="Karnataka",font="Helvetica 15 bold")
    rd3.grid(row=5,column=0)
    rd4=Radiobutton(page2,text="Delhi",variable=var2,value="Delhi",font="Helvetica 15 bold")
    rd4.grid(row=6,column=0)

    btn=Button(page2,text="Next",bg="Blue",foreground="white",command=openNewWindow2)
    btn.grid(row=8,column=5,padx=5,pady=5)
    btn1=Button(page2,text="Quit",bg="red",fg="white",command=root.destroy)
    btn1.grid(row=9,column=5,padx=5,pady=5)
    
def openNewWindow2():
    page3 = Toplevel(root)
    page3.title("Page 3")
    page3.geometry("600x500")
    lbl2=Label(page3,text="Q3.Which city is the capital of india ?",font="Helvetica 15 bold")
    lbl2.grid(row=2,column=0)
    var3=StringVar()
    rd1=Radiobutton(page3,text="Karnataka",variable=var3,value="Maharashtra",font="Helvetica 15 bold")
    rd1.grid(row=3,column=0)
    rd2=Radiobutton(page3,text="Delhi",variable=var3,value="Goa",font="Helvetica 15 bold")
    rd2.grid(row=4,column=0)
    rd3=Radiobutton(page3,text="Jodhpur",variable=var3,value="Karnataka",font="Helvetica 15 bold")
    rd3.grid(row=5,column=0)
    rd4=Radiobutton(page3,text="Goa",variable=var3,value="Delhi",font="Helvetica 15 bold")
    rd4.grid(row=6,column=0)

    btn=Button(page3,text="SUBMIT",bg="black",fg="white",command=done)
    btn.grid(row=8,column=4)
   

def done():
    messagebox.showinfo("Confirmation","Submitted your Response")
    root.destroy()
    


    

heading=Label(root,text="QUIZ",bg="purple",foreground="white",font="comicsansms 24 bold")
heading.grid(row=0,column=5)

lbl1=Label(root,text="Q1.Mumbai located in which state ?",font="Helvetica 15 bold")
lbl1.grid(row=2,column=0)

var1=StringVar()
rd1=Radiobutton(root,text="Maharashtra",variable=var1,value="Maharashtra",font="Helvetica 15 bold")
rd1.grid(row=3,column=0)
rd2=Radiobutton(root,text="Goa",variable=var1,value="Goa",font="Helvetica 15 bold")
rd2.grid(row=4,column=0)
rd3=Radiobutton(root,text="Karnataka",variable=var1,value="Karnataka",font="Helvetica 15 bold")
rd3.grid(row=5,column=0)
rd4=Radiobutton(root,text="Delhi",variable=var1,value="Delhi",font="Helvetica 15 bold")
rd4.grid(row=6,column=0)

btn=Button(root,text="Next",bg="Blue",foreground="white",command=openNewWindow1)
btn.grid(row=8,column=5,padx=5,pady=5)

btn1=Button(root,text="Quit",bg="red",fg="white",command=root.destroy)
btn1.grid(row=9,column=5,padx=5,pady=5)

root.mainloop()
