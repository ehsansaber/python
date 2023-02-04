# Import Module
from tkinter import *

# Create Object
root = Tk()
root.title("Calculater")

# Set geometry
root.geometry('380x220')
root.resizable(0, 0)

#set icon image
photo = PhotoImage(file = "cal_icon.png")
root.iconphoto(False, photo)

#set opration functions
def sum ():
    result.set("") 
    sum_r = number1.get() + number2.get()
    sum_r = str(sum_r)
    result.set("Result is " + sum_r)

def minus ():
    result.set("") 
    minus_r = number1.get() - number2.get()
    minus_r = str(minus_r)
    result.set("Result is " + minus_r) 

def multi ():
    result.set("") 
    multi_r = number1.get() * number2.get()
    multi_r = str(multi_r)
    result.set("Result is " + multi_r) 
    
def division ():
    result.set("") 
    division_r = number1.get() / number2.get()
    division_r = str(division_r)
    result.set("Result is " + division_r) 

def factorial ():
    result.set("") 
    factorial_r = 1
    for i in range(1, int(number1.get())+1):
        factorial_r = factorial_r * i
    factorial_r = str(factorial_r)
    result.set("Result is " + factorial_r) 
    
def radical ():
    result.set("") 
    radical_r = number1.get() ** (1/2)
    radical_r = str(radical_r)
    result.set("Result is " + radical_r) 

def power ():
    result.set("") 
    power_r = number1.get() ** number2.get()
    power_r = str(power_r)
    result.set("Result is " + power_r) 

def absolute_value ():
    result.set("") 
    if number1.get() < 0 :
        absolute_value_r = -number1.get()
    else :
        absolute_value_r = number1.get()
    absolute_value_r = str(absolute_value_r)
    result.set("Result is " + absolute_value_r) 

#add frames
frame = Frame()
frame.pack(pady=10)

frame1 = Frame()
frame1.pack()

frame2 = Frame()
frame2.pack(pady=10)

frame3 = Frame()
frame3.pack(pady=10)

frame4 = Frame()
frame4.pack(pady=10)

#add inputs
number1 = DoubleVar()
number2 = DoubleVar()

#add output
result = StringVar()

#add labels and entry for inputs
Label(frame, text = 'Number1', font='Caveat 10 bold').pack(side=LEFT)
Entry(frame, textvariable = number1, width=50).pack()

Label(frame1, text = 'Number2', font='Caveat 10 bold').pack(side=LEFT)
Entry(frame1, textvariable = number2, width=50).pack()

Label(frame2, textvariable=result, font='Caveat 10 bold').pack(side=LEFT)

#add oprations button
sum_btn = Button(frame3, text="+", command=sum, width=7, bg="powderblue", fg="black")
sum_btn.pack(side=LEFT, padx=5)

minus_btn = Button(frame3, text="-", command=minus, width=7, bg="powderblue", fg="black")
minus_btn.pack(side=LEFT, padx=5)

multi_btn = Button(frame3, text="x", command=multi, width=7, bg="powderblue", fg="black")
multi_btn.pack(side=LEFT, padx=5)

division_btn = Button(frame3, text="÷", command=division, width=7, bg="powderblue", fg="black")
division_btn.pack(side=LEFT, padx=5)

factorial_btn = Button(frame4, text="n!", command=factorial, width=7, bg="powderblue", fg="black")
factorial_btn.pack(side=LEFT, padx=5)

radical_btn = Button(frame4, text="√", command=radical, width=7, bg="powderblue", fg="black")
radical_btn.pack(side=LEFT, padx=5)

power_btn = Button(frame4, text="^", command=power, width=7, bg="powderblue", fg="black")
power_btn.pack(side=LEFT, padx=5)

absolute_value_btn = Button(frame4, text="|n|", command=absolute_value, width=7, bg="powderblue", fg="black")
absolute_value_btn.pack(side=LEFT, padx=5)

# Execute Tkinter
root.mainloop()

