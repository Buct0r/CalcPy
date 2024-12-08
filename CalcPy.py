from tkinter import *
from math import sqrt, pow

def press(num):
    global equation 

    equation += str(num)
    label.set(equation) 

    if len(equation) >= 44:
        label.set("Error: too many digits")
        equation = ""

def equals():
    try:
        global equation

        total = str(eval(equation))

        total = float(total)

        if total%1 != 0:
            total = str(total)
            label.set(total)
        else:
            total = f"{total:.0f}"
            label.set(total)

        equation = total
    except ZeroDivisionError:
        label.set("Error")
        equation = ""
    except SyntaxError:
        label.set("Syntax Error")
        equation = ""
    except TypeError:
        label.set("Syntax Error")
        equation = ""

    if len(equation) >= 44:
        label.set("Error: too many digits")
        equation = ""


def clear():
    global equation

    label.set("0")

    equation = ""

def cancel():
    global equation

    equation = equation[:-1]

    if equation == "":
        label.set("0")
    else:
        label.set(equation)

def turnOff():
    window.destroy()

def turn_negative():
    global equation
    equation = float(equation)* -1
    if equation%1 != 0:
        equation = str(equation)
    else:
        equation = f"{equation:.0f}"
    label.set(equation)
    
def power():
    global equation

    equation = float(equation)
    try:
        equation = pow(equation, 2)
    except OverflowError:
        equation = "Too many digits"
    try:    
        if equation%1 != 0:
            equation = str(equation)
            label.set(equation)
        else:
            equation = f"{equation:.0f}"
            label.set(equation)
    except TypeError:
        label.set(equation)
        equation = ""
    if len(equation) >= 44:
        label.set("Error: too many digits")
        equation = ""

def squareRoot():
    global equation

    equation = float(equation)
    equation = sqrt(equation)    
    if equation%1 != 0:
        equation = str(equation)
    else:
        equation = f"{equation:.0f}"
    
    label.set(equation)
    if len(equation) >= 44:
        label.set("Error: too many digits")
        equation = ""


window = Tk()
window.geometry("370x470")
window.resizable(False, False)
window.config(bg="#353536")
window.title("CalcPy")

equation = ""
label = StringVar()

label.set("0")

text = Label(window)
text.config(textvariable=label, bg="#566650", bd=3, width=39, height=5, relief=SUNKEN, anchor="e", font=('Arial', 11)) #cambiare colori quando tasti premuti


text.pack(pady=5)

frame2 = Frame(window)
frame2.pack()

button_clear = Button(frame2, font=("Arial", 10, "bold"),text="←", height=3, width=10, command= cancel, bg="#818182")
button_clear.grid(row=0, column=3)

button_cancel = Button(frame2, font=("Arial", 10, "bold"), text="C", height=3, width=10, command= clear, bg="#818182")
button_cancel.grid(row=0, column=2)

button_off = Button(frame2, font=("Arial", 10, "bold"), text="OFF", height=3, width=10, command= turnOff, bg="#818182")
button_off.grid(row=0, column=0)

button_plus_minus = Button(frame2, font=("Arial", 10, "bold"),text="-/+", height=3, width=10, command= turn_negative, bg="#818182")
button_plus_minus.grid(row=0, column=1)

button_parentesis_open = Button(frame2, font=("Arial", 10, "bold"),text="(", height=3, width=10, command= lambda: press("("), bg="#818182")
button_parentesis_open.grid(row=1,column=2)

button_parentesis_close = Button(frame2, font=("Arial", 10, "bold"),text=")", height=3, width=10, command= lambda: press(")"), bg="#818182")
button_parentesis_close.grid(row=1,column=3)

button_power = Button(frame2, font=("Arial", 10, "bold"),text="x^2", height=3, width=10, command= power, bg="#818182")
button_power.grid(row=1, column=0)

button_sqrt = Button(frame2, font=("Arial", 10, "bold"),text="√x", height=3, width=10, command= squareRoot, bg="#818182")
button_sqrt.grid(row=1, column=1)

frame = Frame(window)
frame.pack()


button_0 = Button(frame, font=("Arial", 10, "bold"), text=0, height=3, width=10, command= lambda: press(0), bg="#818182")
button_0.grid(row=3, column=0)

button_1 = Button(frame, font=("Arial", 10, "bold"), text=1, height=3, width=10, command= lambda: press(1), bg="#818182")
button_1.grid(row=2, column=0)
 
button_2 = Button(frame, font=("Arial", 10, "bold"), text=2, height=3, width=10, command= lambda: press(2), bg="#818182")
button_2.grid(row=2, column=1)

button_3 = Button(frame, font=("Arial", 10, "bold"),text=3, height=3, width=10, command= lambda: press(3), bg="#818182")
button_3.grid(row=2, column=2)

button_4 = Button(frame, font=("Arial", 10, "bold"),text=4, height=3, width=10, command= lambda: press(4), bg="#818182")
button_4.grid(row=1, column=0)

button_5 = Button(frame, font=("Arial", 10, "bold"),text=5, height=3, width=10, command= lambda: press(5), bg="#818182")
button_5.grid(row=1, column=1)

button_6 = Button(frame, font=("Arial", 10, "bold"),text=6, height=3, width=10, command= lambda: press(6), bg="#818182")
button_6.grid(row=1, column=2)

button_7 = Button(frame, font=("Arial", 10, "bold"),text=7, height=3, width=10, command= lambda: press(7), bg="#818182")
button_7.grid(row=0, column=0)

button_8 = Button(frame, font=("Arial", 10, "bold"),text=8, height=3, width=10, command= lambda: press(8), bg="#818182")
button_8.grid(row=0, column=1)

button_9 = Button(frame,font=("Arial", 10, "bold"), text=9, height=3, width=10, command= lambda: press(9), bg="#818182")
button_9.grid(row=0, column=2)

button_plus = Button(frame, font=("Arial", 10, "bold"),text="+", height=3, width=10, command= lambda: press("+"), bg="#818182")
button_plus.grid(row=3, column=3)

button_minus = Button(frame, font=("Arial", 10, "bold"),text="-", height=3, width=10, command= lambda: press("-"), bg="#818182")
button_minus.grid(row=2, column=3)

button_times = Button(frame, font=("Arial", 10, "bold"),text="*", height=3, width=10, command= lambda: press("*"), bg="#818182")
button_times.grid(row=1, column=3)

button_divid = Button(frame, font=("Arial", 10, "bold"),text="/", height=3, width=10, command= lambda: press("/"), bg="#818182")
button_divid.grid(row=0, column=3)

button_equals = Button(frame, font=("Arial", 10, "bold"),text="=", height=3, width=10, command= equals, bg="#818182")
button_equals.grid(row=3, column=2)

button_decimal = Button(frame, font=("Arial", 10, "bold"),text=".", height=3, width=10, command= lambda: press("."), bg="#818182")
button_decimal.grid(row=3, column=1)

window.mainloop()