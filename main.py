from tkinter import *
from decimal import *

BUTTON_HEIGHT = 4
BUTTON_WIDTH = BUTTON_HEIGHT*3
PADDING = BUTTON_HEIGHT * 2

root = Tk()
root.title("Calculator")

text_field = Entry(root, width=BUTTON_WIDTH*4, borderwidth=5)
text_field.grid(row=0, column=1, columnspan=4, padx=PADDING, pady=PADDING)


def number(number):
    current = text_field.get()
    text_field.delete(0, END)
    text_field.insert(0, str(current) + str(number))


def delete():
    text_field.delete(0, END)
    global first_number
    first_number = 0    


def add():
    global first_number
    global sign
    first_number = text_field.get()
    sign = "add"
    text_field.delete(0, END)


def subtract():
    global first_number
    global sign
    first_number = text_field.get()
    sign = "subtract"
    text_field.delete(0, END)


def multiple():
    global first_number
    global sign
    first_number = text_field.get()
    sign = "multiple"
    text_field.delete(0, END)


def divide():
    global first_number
    global sign
    first_number = text_field.get()
    sign = "divide"
    text_field.delete(0, END)


def percent():
    first_number = text_field.get()
    result = Decimal(first_number) / 100
    text_field.delete(0, END)
    text_field.insert(0, result)


def value():
    first_number = text_field.get()
    if "-" in first_number:
        result = first_number.removeprefix("-")
    elif "-" not in first_number:
        result = "-" + first_number
    text_field.delete(0, END)
    text_field.insert(0, result)


def coma():
    current = text_field.get()
    if "." not in current:
        text_field.insert(END, ".")
    

def equal():
    second_number = text_field.get()
    text_field.delete(0, END)

    if sign == "add":
        result = Decimal(first_number) + Decimal(second_number)
        text_field.insert(0, result)

    elif sign == "subtract":
        result = Decimal(first_number) - Decimal(second_number)
        text_field.insert(0, result)

    elif sign == "multiple":
        result = Decimal(first_number) * Decimal(second_number)
        text_field.insert(0, result)

    elif sign == "divide":
        result = Decimal(first_number) / Decimal(second_number)
        text_field.insert(0, result)


button_0 = Button(root, text="0", width=BUTTON_WIDTH*2, height=BUTTON_HEIGHT, command=lambda: number(0)).grid(row=5, column=0, columnspan=2, padx=PADDING, pady=PADDING)
button_coma = Button(root, text=",", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command=coma).grid(row=5, column=2, padx=PADDING, pady=PADDING)
button_equal = Button(root, text="=", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command=equal).grid(row=5, column=3, padx=PADDING, pady=PADDING)

button_1 = Button(root, text="1", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command=lambda: number(1)).grid(row=4, column=0, padx=PADDING, pady=PADDING)
button_2 = Button(root, text="2", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command=lambda: number(2)).grid(row=4, column=1, padx=PADDING, pady=PADDING)
button_3 = Button(root, text="3", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command=lambda: number(3)).grid(row=4, column=2, padx=PADDING, pady=PADDING)
button_add = Button(root, text="+", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command=add).grid(row=4, column=3, padx=PADDING, pady=PADDING)

button_4 = Button(root, text="4", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command=lambda: number(4)).grid(row=3, column=0, padx=PADDING, pady=PADDING)
button_5 = Button(root, text="5", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command=lambda: number(5)).grid(row=3, column=1, padx=PADDING, pady=PADDING)
button_6 = Button(root, text="6", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command=lambda: number(6)).grid(row=3, column=2, padx=PADDING, pady=PADDING)
button_subtract = Button(root, text="-", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command=subtract).grid(row=3, column=3, padx=PADDING, pady=PADDING)

button_7 = Button(root, text="7", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command=lambda: number(7)).grid(row=2, column=0, padx=PADDING, pady=PADDING)
button_8 = Button(root, text="8", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command=lambda: number(8)).grid(row=2, column=1, padx=PADDING, pady=PADDING)
button_9 = Button(root, text="9", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command=lambda: number(9)).grid(row=2, column=2, padx=PADDING, pady=PADDING)
button_multiple = Button(root, text="x", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command=multiple).grid(row=2, column=3, padx=PADDING, pady=PADDING)

button_clear = Button(root, text="AC", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command=delete).grid(row=1, column=0, padx=PADDING, pady=PADDING)
button_value = Button(root, text="+/-", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command=value).grid(row=1, column=1, padx=PADDING, pady=PADDING)
button_percent = Button(root, text="%", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command=percent).grid(row=1, column=2, padx=PADDING, pady=PADDING)
button_divide = Button(root, text="÷", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command=divide).grid(row=1, column=3, padx=PADDING, pady=PADDING)


root.mainloop()