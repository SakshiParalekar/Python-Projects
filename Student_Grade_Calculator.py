import tkinter
from tkinter import *


def calculate():
    english=int(englishentry.get())
    skills=int(skillentry.get())
    general=int(generalentry.get())
    total=(english+skills+general)
    Label(text=f"{total}",font="arial 15").place(x=250,y=170)
    average=total/3
    Label(text=f"{average}",font="arial 15").place(x=250,y=210)

    if average>50:
        grade="PASS"
    else:
        grade="FAIL"

    Label(text=f"{grade}",font="arial 15 bold",fg="blue").place(x=250,y=260)



root=Tk()
root.title("Grade Calculator")
root.geometry("500x400")
#root.config(background=" grey")

sub1=Label(root,text="English",font="arial 10")
sub2=Label(root,text="Analytical Skill",font="arial 10")

sub3=Label(root,text="General Knowledge",font="arial 10")
total=Label(root,text="Total")
avg=Label(root,text="Average")
grade=Label(root,text="Grade")

sub1.place(x=50,y=20)
sub2.place(x=50,y=70)
sub3.place(x=50,y=120)
total.place(x=50,y=170)
avg.place(x=50,y=220)
grade.place(x=50,y=270)

var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=IntVar()

englishentry=Entry(root,textvariable=var1,font="arial 15")
skillentry=Entry(root,textvariable=var2,font="arial 15")
generalentry=Entry(root,textvariable=var3,font="arial 15")

englishentry.place(x=250,y=20)
skillentry.place(x=250,y=70)
generalentry.place(x=250,y=120)


cal=Button(root,text="Calculate",bd=10,bg="white",command=calculate)
cal.place(x=50,y=300)
ex=Button(root,text="Exit",bg="white",bd=10,padx=10,command=lambda:exit())
ex.place(x=350,y=300)


root.mainloop()


