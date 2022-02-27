from tkinter import *
import random
import time

# root window
root = Tk()
root.geometry('1600x700+00') # appear on x=0, y=0 of screen
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