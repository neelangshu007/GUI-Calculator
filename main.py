# import everything from tkinter module
from tkinter import *

# create a GUI window
root = Tk()

# set the title of GUI window
root.title("Simple Calculator")

# Tkinter GUI App Icon
root.iconbitmap("assets/calculator2.ico")

# set the configuration of GUI window
root.geometry("301x507")

total = 0

# globally declare the expression variable
math_sign = " "


# Function to handle button click
def button_click(number):
    current = inputField.get()
    inputField.delete(0, END)
    inputField.insert(0, str(current) + str(number))


# Function to clear the contents
# of text entry box
def button_clear():
    inputField.delete(0, END)


# Function to evaluate add
def button_add():
    first_number = inputField.get()
    global total
    global math_sign
    math_sign = "addition"
    total = float(first_number)
    inputField.delete(0, END)


# Function to evaluate minus
def button_minus():
    first_number = inputField.get()
    global total
    global math_sign
    math_sign = "minus"
    total = float(first_number)
    inputField.delete(0, END)


# Function to evaluate divide
def button_divide():
    first_number = inputField.get()
    global total
    global math_sign
    math_sign = "divide"
    total = float(first_number)
    inputField.delete(0, END)


# Function to evaluate multiplication
def button_multi():
    first_number = inputField.get()
    global total
    global math_sign
    math_sign = "multiply"
    total = float(first_number)
    inputField.delete(0, END)


# Function to evaluate power
def button_power():
    first_number = inputField.get()
    global total
    global math_sign
    math_sign = "power"
    total = float(first_number)
    inputField.delete(0, END)


# Function to evaluate percentage
def button_percentage():
    first_number = inputField.get()
    inputField.delete(0, END)
    inputField.insert(0, float(first_number) / 100)


# Function to evaluate the final expression
def button_equal():
    second_number = inputField.get()
    inputField.delete(0, END)
    if math_sign == "addition":
        inputField.insert(0, total + float(second_number))
    elif math_sign == "minus":
        inputField.insert(0, total - float(second_number))
    elif math_sign == "multiply":
        inputField.insert(0, total * float(second_number))
    elif math_sign == "power":
        inputField.insert(0, pow(total, float(second_number)))
    elif math_sign == "divide":

        # Try and except statement is used
        # for handling the errors like zero
        # division error etc.

        # Put that code inside the try block
        # which may generate the error
        try:
            inputField.insert(0, total / float(second_number))

        # if error is generate then handle
        # by the except block
        except:
            inputField.insert(0, "INVALID")
            # inputField.delete(0, END)


# create the text entry box for
# showing the expression .
inputField = Entry(root, width=45, borderwidth=5)

# grid method is used for placing
# the widgets at respective positions
# in table like structure .
inputField.grid(row=0, column=0, columnspan=3, padx=10, pady=15)

# create a Buttons and place at a particular
# location inside the root window .
# when user press the button, the command or
# function affiliated to that button is executed .
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
buttonPulse = Button(root, text="+", padx=39, pady=20, command=button_add)
buttonEqual = Button(root, text="=", padx=40, pady=20, command=button_equal)
buttonClear = Button(root, text="Clear", padx=130, pady=20, command=button_clear)
buttonMinus = Button(root, text="-", padx=41, pady=20, command=button_minus)
buttonDivide = Button(root, text="/", padx=40, pady=20, command=button_divide)
buttonMulti = Button(root, text="*", padx=40, pady=20, command=button_multi)
buttonPower = Button(root, text="x^y", padx=33, pady=20, command=button_power)
buttonPercentage = Button(root, text="%", padx=38, pady=20, command=button_percentage)
buttonPoint = Button(root, text=".", padx=42, pady=20, command=lambda: button_click("."))

button0.grid(row=4, column=0)
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
buttonPulse.grid(row=4, column=1)
buttonEqual.grid(row=6, column=2)
buttonMulti.grid(row=5, column=0)
buttonDivide.grid(row=5, column=1)
buttonMinus.grid(row=4, column=2)
buttonPower.grid(row=6, column=0)
buttonPercentage.grid(row=6, column=1)
buttonClear.grid(row=7, column=0, columnspan=3)
buttonPoint.grid(row=5, column=2)

# start the GUI
root.mainloop()
