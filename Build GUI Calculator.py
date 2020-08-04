from tkinter import *

window=Tk()
window.title("My Calculator")
window.config(bg="gray")

e=Entry(window,width=35,bd=5,bg="light gray",fg="black")
e.grid(row=0,column=0,padx=10,pady=10,columnspan=3)

def add(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def clear():
    e.delete(0,END)

def additon():
    first=e.get()
    global f_num
    global math
    math="addition"
    f_num=int(first)
    e.delete(0,END)

def equal():
    second=e.get()
    e.delete(0,END)
    if math=="addition":
        e.insert(0,f_num+int(second))

    if math=="subtraction":
        e.insert(0,f_num-int(second))

    if math=="division":
        e.insert(0,f_num/int(second))

    if math=="multiplication":
        e.insert(0,f_num*int(second))


def subtract():
    first=e.get()
    global f_num
    global math
    math="subtraction"
    f_num=int(first)
    e.delete(0,END)

def divide():
    first=e.get()
    global f_num
    global math
    math="division"
    f_num=int(first)
    e.delete(0,END)

def multiply():
    first=e.get()
    global f_num
    global math
    math="multiplication"
    f_num=int(first)
    e.delete(0,END)

button_1=Button(window,text="1",activebackground="red",padx=30,pady=20,command=lambda:add(1))
button_2=Button(window,text="2",padx=30,pady=20,command=lambda:add(2))
button_3=Button(window,text="3",padx=30,pady=20,command=lambda:add(3))

button_4=Button(window,text="4",padx=30,pady=20,command=lambda:add(4))
button_5=Button(window,text="5",padx=30,pady=20,command=lambda:add(5))
button_6=Button(window,text="6",padx=30,pady=20,command=lambda:add(6))

button_7=Button(window,text="7",padx=30,pady=20,command=lambda:add(7))
button_8=Button(window,text="8",padx=30,pady=20,command=lambda:add(8))
button_9=Button(window,text="9",padx=30,pady=20,command=lambda:add(9))

button_0=Button(window,text="0",padx=30,pady=20,command=lambda:add(0))
button_add=Button(window,text="+",padx=29,pady=20,command=additon)
button_equal=Button(window,text="=",padx=80,pady=20,command=equal)
button_clear=Button(window,text="clear",padx=70,pady=20,command=clear)

button_substract=Button(window,text="-",padx=32,pady=20,command=subtract)
button_divide=Button(window,text="/",padx=32,pady=20,command=divide)
button_multiply=Button(window,text="*",padx=32,pady=20,command=multiply)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_add.grid(row=5,column=0)
button_clear.grid(row=4,column=1,columnspan=2)
button_equal.grid(row=5,column=1,columnspan=2)

button_substract.grid(row=6,column=0)
button_divide.grid(row=6,column=1)
button_multiply.grid(row=6,column=2)



window.mainloop()