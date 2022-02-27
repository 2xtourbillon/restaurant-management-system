from ast import Str
from asyncore import file_dispatcher
from pickletools import stringnl_noescape
from tkinter import *
import random
import time

# root window
root = Tk()
root.geometry('1600x700+0+0') # appear on x=0, y=0 of screen
root.title('Restuarant Management System')

# main frame
Tops = Frame(root, bg='black', width=1600, height=500, relief=SUNKEN)
Tops.pack(side=TOP)

# left frame
f1 = Frame(root, width=900, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

# right frame
f2 = Frame(root, width=400, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)

# .asctime() convert struct_time to 24char str
# .localtime() converts # of seconds to local time
# .time() returns time from beginning of epoch in seconds
localtime = time.asctime(time.localtime(time.time()))
lblinfo = Label(Tops, font=('Aria', 30, 'bold'), text='Restaurant Management System', 
                fg='blue', bd=10, anchor='w')
lblinfo.grid(row=0, column=0)
lblinfo = Label(Tops, font=('aria', 30, 'bold'), text=localtime, fg='red', anchor='w')
lblinfo.grid(row=1, column=0)

text_Input = StringVar()
operator = ''

# text display of calculator
txtdisplay = Entry(f2, font=('arial', 20, 'bold'), textvariable=text_Input, bd=5, 
                    insertwidth=7, bg='green', justify='right')
txtdisplay.grid(columnspan=4)

# button #7
btn7 = Button(f2, padx=16, pady=16, bd=4, fg='white', font=('arial', 20, 'bold'),
              text='7', ng='black', command=lambda: btnclick(7))
btn7.grid(row=2, column=0)

# button #8
btn8 = Button(f2, padx=16, pady=16, bd=4, fg='white', font=('arial', 20, 'bold'),
              text='8', ng='black', command=lambda: btnclick(8))
btn8.grid(row=2, column=1)

# button #9
btn9 = Button(f2, padx=16, pady=16, bd=4, fg='white', font=('arial', 20, 'bold'),
              text='9', ng='black', command=lambda: btnclick(9))
btn9.grid(row=2, column=2)

# additional
Addition = Button(f2, padx=16, pady=16, bd=4, fg='white', font=('arial', 20, 'bold'),
              text='+', ng='black', command=lambda: btnclick("+"))
Addition.grid(row=2, column=3)

# button #4
btn4 = Button(f2, padx=16, pady=16, bd=4, fg='white', font=('arial', 20, 'bold'),
              text='4', ng='black', command=lambda: btnclick(4))
btn4.grid(row=3, column=0)

# button #5
btn5 = Button(f2, padx=16, pady=16, bd=4, fg='white', font=('arial', 20, 'bold'),
              text='5', ng='black', command=lambda: btnclick(5))
btn5.grid(row=3, column=1)

# button #6
btn6 = Button(f2, padx=16, pady=16, bd=4, fg='white', font=('arial', 20, 'bold'),
              text='6', ng='black', command=lambda: btnclick(6))
btn6.grid(row=3, column=2)

# Subtraction
Subtraction = Button(f2, padx=16, pady=16, bd=4, fg='white', font=('arial', 20, 'bold'),
              text='-', ng='black', command=lambda: btnclick("-"))
Subtraction.grid(row=3, column=3)

# button #1
btn1 = Button(f2, padx=16, pady=16, bd=4, fg='white', font=('arial', 20, 'bold'),
              text='1', ng='black', command=lambda: btnclick(1))
btn1.grid(row=4, column=0)

# button #2
btn2 = Button(f2, padx=16, pady=16, bd=4, fg='white', font=('arial', 20, 'bold'),
              text='2', ng='black', command=lambda: btnclick(2))
btn2.grid(row=4, column=1)

# button #3
btn3 = Button(f2, padx=16, pady=16, bd=4, fg='white', font=('arial', 20, 'bold'),
              text='3', ng='black', command=lambda: btnclick(3))
btn3.grid(row=4, column=2)

# Multiply
multiply = Button(f2, padx=16, pady=16, bd=4, fg='white', font=('arial', 20, 'bold'),
              text='Multuply', ng='black', command=lambda: btnclick("*"))
multiply.grid(row=4, column=3)

# button #0
btn0 = Button(f2, padx=16, pady=16, bd=4, fg='white', font=('arial', 20, 'bold'),
              text='0', ng='black', command=lambda: btnclick(0))
btn0.grid(row=5, column=0)

# Clear
btnc = Button(f2, padx=16, pady=16, bd=4, fg='white', font=('arial', 20, 'bold'),
              text='c', ng='black', command=clrdisplay)
btnc.grid(row=5, column=1)

# decimal
decimal = Button(f2, padx=16, pady=16, bd=4, fg='white', font=('arial', 20, 'bold'),
              text='.', ng='black', command=lambda: btnclick("."))
decimal.grid(row=5, column=2)

# division
division = Button(f2, padx=16, pady=16, bd=4, fg='white', font=('arial', 20, 'bold'),
              text='/', ng='black', command=lambda: btnclick('/'))
division.grid(row=5, column=3)

# equal to
btnequal = Button(f2, padx=16, pady=16, bd=4, fg='white', font=('arial', 20, 'bold'),
              text='=', ng='black', command=equals)
btnequal.grid(columnspan=4)


# items
rand = StringVar()
Fries = StringVar()
LargeFries = StringVar()
Burger = StringVar()
Filet = StringVar()
SubTotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
Cost = StringVar()
Cheese_Burger = StringVar()

# order label
lblreference = Label(f1, font=('aria', 16, 'bold'), text='Order No.', fg='black', bd=10, anchor='w')
lblreference.grid(row=0, column=0)

txtreference = Entry(f1, font=('arial', 17, 'bold'), textvariable=rand, bd=6, insertwidth=4, bg='red', justify='right')
txtreference.grid(row=1, column=1)

# fries
lblfries = Label(f1, font=('aria', 16, 'bold'), text='Fries Meal', fg='black', bd=10, anchor='w')
lblfries.grid(row=1, column=0)
txtfries = Entry(f1, font=('arial', 17, 'bold'), textvariable=Fries, bd=6, insertwidth=4, bg='red', justify='right')
txtfries.grid(row=1, column=1)

# large fries
lblLargefries = Label(f1, font=('aria', 16, 'bold'), text='Lunch Meal', fg='black', bd=10, anchor='w')
lblLargefries.grid(row=2, column=0)
txtLargefries = Entry(f1, font=('arial', 17, 'bold'), textvariable=LargeFries, bd=6, insertwidth=4, bg='red', justify='right')
txtLargefries.grid(row=2, column=1)

# burger
lblburger = Label(f1, font=('aria', 16, 'bold'), text='Burger Meal', fg='black', bd=10, anchor='w')
lblburger.grid(row=3, column=0)
txtburger = Entry(f1, font=('arial', 17, 'bold'), textvariable=Burger, bd=6, insertwidth=4, bg='red', justify='right')
txtburger.grid(row=3, column=1)

# Filet
lblFilet = Label(f1, font=('aria', 16, 'bold'), text='Pizza Meal', fg='black', bd=10, anchor='w')
lblFilet.grid(row=4, column=0)
txtFilet = Entry(f1, font=('arial', 17, 'bold'), textvariable=Filet, bd=6, insertwidth=4, bg='red', justify='right')
txtFilet.grid(row=4, column=1)

# Cheese Burger
lblCheeseBurger = Label(f1, font=('aria', 16, 'bold'), text='Cheese Burger', fg='black', bd=10, anchor='w')
lblCheeseBurger.grid(row=5, column=0)
txtCheeseBurger = Entry(f1, font=('arial', 17, 'bold'), textvariable=Cheese_Burger, bd=6, insertwidth=4, bg='red', justify='right')
txtCheeseBurger.grid(row=5, column=1)

# Drinks
lblDrinks = Label(f1, font=('aria', 16, 'bold'), text='Drinks', fg='black', bd=10, anchor='w')
lblDrinks.grid(row=0, column=2)
txtDrinks = Entry(f1, font=('arial', 17, 'bold'), textvariable=Drinks, bd=6, insertwidth=4, bg='red', justify='right')
txtDrinks.grid(row=0, column=3)

# Cost
lblCost = Label(f1, font=('aria', 16, 'bold'), text='Cost', fg='black', bd=10, anchor='w')
lblCost.grid(row=1, column=2)
txtCost = Entry(f1, font=('arial', 17, 'bold'), textvariable=Cost, bd=6, insertwidth=4, bg='red', justify='right')
txtCost.grid(row=1, column=3)

# Service Charge
lblService_Charge = Label(f1, font=('aria', 16, 'bold'), text='Service Charge', fg='black', bd=10, anchor='w')
lblService_Charge.grid(row=2, column=2)
txtService_Charge = Entry(f1, font=('arial', 17, 'bold'), textvariable=Service_Charge, bd=6, insertwidth=4, bg='red', justify='right')
txtService_Charge.grid(row=2, column=3)

# Tax
lblTax = Label(f1, font=('aria', 16, 'bold'), text='Tax', fg='black', bd=10, anchor='w')
lblTax.grid(row=3, column=2)
txtTax = Entry(f1, font=('arial', 17, 'bold'), textvariable=Tax, bd=6, insertwidth=4, bg='red', justify='right')
txtTax.grid(row=3, column=3)

# Subtotal
lblSubtotal = Label(f1, font=('aria', 16, 'bold'), text='Subtotal', fg='black', bd=10, anchor='w')
lblSubtotal.grid(row=4, column=2)
txtSubtotal = Entry(f1, font=('arial', 17, 'bold'), textvariable=SubTotal, bd=6, insertwidth=4, bg='red', justify='right')
txtSubtotal.grid(row=4, column=3)

# Total
lblTotal = Label(f1, font=('aria', 16, 'bold'), text='Total', fg='black', bd=10, anchor='w')
lblTotal.grid(row=5, column=2)
txtTotal = Entry(f1, font=('arial', 17, 'bold'), textvariable=Total, bd=6, insertwidth=4, bg='red', justify='right')
txtTotal.grid(row=5, column=3)

# Total button
btnTotal = Button(f1, padx=16, pady=8, bd=10, fg='black', font=('Arial', 16, 'bold'), width=10, text='TOTAL', bg='powder blue', command=Ref)
btnTotal.grid(row=7, column=1)

# Reset Button
btnReset = Button(f1, padx=16, pady=8, bd=10, fg='black', font=('Arial', 16, 'bold'), width=10, text='RESET', bg='powder blue', command=reset)
btnReset.grid(row=7, column=2)

# Exit Button
btnExit = Button(f1, padx=16, pady=8, bd=10, fg='black', font=('Arial', 16, 'bold'), width=10, text='EXIT', bg='powder blue', command=exit)
btnExit.grid(row=7, column=3)

# Price Button
btnPrice = Button(f1, padx=16, pady=8, bd=10, fg='black', font=('Arial', 16, 'bold'), width=10, text='PRICE', bg='powder blue', command=price)
btnPrice.grid(row=7, column=4)

root.mainloop()