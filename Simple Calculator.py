from tkinter import *

root = Tk()

display = Entry(root, width = 35)
display.grid(row = 0, column = 0, columnspan = 4, pady = 10)


def solve(num):
    current = display.get()
    display.delete(0, END)
    display.insert(0, str(current) + str(num))

def clear():
    display.delete(0, END)

def operator(op):
    num1 = display.get()
    global firstNum
    global ope
    ope = op
    firstNum = float(num1)
    display.delete(0, END)

def equal():
    global num2
    num2 = display.get()
    display.delete(0, END)
    if ope == "add":
        #add()
        secNum = float(num2)
        result = firstNum + secNum
        display.insert(0, str(result))
    elif ope == "times":
        #times()
        secNum = float(num2)
        result = firstNum * secNum
        display.insert(0, str(result))
    elif ope == "div":
        #divide()
        secNum = float(num2)
        result = firstNum / secNum
        display.insert(0, str(result))
    elif ope == "minus":
        secNum = float(num2)
        result = firstNum - secNum
        display.insert(0, str(result))

    
c1 = Button(root, text = "1", padx = 20, pady = 10, command = lambda: solve(1))
c2 = Button(root, text = "2", padx = 20, pady = 10, command = lambda: solve(2))
c3 = Button(root, text = "3", padx = 20, pady = 10, command = lambda: solve(3))
c4 = Button(root, text = "4", padx = 20, pady = 10, command = lambda: solve(4))
c5 = Button(root, text = "5", padx = 20, pady = 10, command = lambda: solve(5))
c6 = Button(root, text = "6", padx = 20, pady = 10, command = lambda: solve(6))
c7 = Button(root, text = "7", padx = 20, pady = 10, command = lambda: solve(7))
c8 = Button(root, text = "8", padx = 20, pady = 10, command = lambda: solve(8))
c9 = Button(root, text = "9", padx = 20, pady = 10, command = lambda: solve(9))
c0 = Button(root, text = "0", padx = 20, pady = 10, command = lambda: solve(0))
clear = Button(root, text = "clear", padx = 14, pady = 10, command = clear)
add = Button(root, text = "+", padx = 20, pady = 10, command = lambda: operator("add"))
equal = Button(root, text = "=", padx = 20, pady = 10, command = equal)
multiply = Button(root, text = "*", padx = 20, pady = 10, command = lambda: operator("times"))
divide = Button(root, text = "/", padx = 20, pady = 10, command = lambda: operator("div"))
subtract = Button(root, text = "-", padx = 20, pady = 10, command = lambda: operator("minus"))

c7.grid(row = 1, column = 0)
c8.grid(row = 1, column = 1)
c9.grid(row = 1, column = 2)
multiply.grid(row = 1, column = 3)

c4.grid(row = 2, column = 0)
c5.grid(row = 2, column = 1)
c6.grid(row = 2, column = 2)
divide.grid(row = 2, column = 3)

c1.grid(row = 3, column = 0)
c2.grid(row = 3, column = 1)
c3.grid(row = 3, column = 2)
subtract.grid(row = 3, column = 3)

clear.grid(row = 4, column = 0)
c0.grid(row = 4, column = 1)
add.grid(row = 4, column = 2)
equal.grid(row = 4, column = 3)

root.mainloop()
