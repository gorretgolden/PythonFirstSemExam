#GUI Calculator application using Tkinter
from tkinter import *
from turtle import color
from typing import Match
root = Tk()
root.title('Calculator Application')

#entry widget 
e = Entry(root,borderwidth=5,width=35)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)


#functions to add, subtract, multiply, divide and modulus
def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0,END)

def button_add():
   initial_number =  e.get()  
   global second_number 
   global math
   math = "addition"
   second_number = int(initial_number)
   e.delete(0,END)
   
def button_equals():
    last_value = e.get()  
    e.delete(0, END) 
    if math == "addition":
      e.insert(0,second_number + int(last_value))
   
    if math == "subtraction":
          e.insert(0,second_number - int(last_value))
   
    if math == "division":
          e.insert(0,second_number / int(last_value))
   
    if math == "multiplication":
          e.insert(0,second_number * int(last_value))
          
    if math == "modulus":
          e.insert(0,second_number % int(last_value))
    
   
def button_subtract():
   initial_number =  e.get()  
   global second_number 
   global math
   math = "subtraction"
   second_number = int(initial_number)
   e.delete(0,END)
   
    
def button_divide():
   initial_number =  e.get()  
   global second_number 
   global math
   math = "division"
   second_number = int(initial_number)
   e.delete(0,END)
     
        
def button_multiply():
   initial_number =  e.get()  
   global second_number 
   global math
   math = "multiplication"
   second_number = int(initial_number)
   e.delete(0,END)

def button_modulus():
   initial_number =  e.get()  
   global second_number 
   global math
   math = "modulus"
   second_number = int(initial_number)
   e.delete(0,END)
        
#buttons 
button_1 = Button(root,text=1,padx=40,pady=20,command=lambda:button_click(1))
button_2 = Button(root,text=2,padx=40,pady=20,command=lambda:button_click(2))
button_3 = Button(root,text=3,padx=40,pady=20,command=lambda:button_click(3))
button_4 = Button(root,text=4,padx=40,pady=20,command=lambda:button_click(4))
button_5 = Button(root,text=5,padx=40,pady=20,command=lambda:button_click(5))
button_6 = Button(root,text=6,padx=40,pady=20,command=lambda:button_click(6))
button_7 = Button(root,text=7,padx=40,pady=20,command=lambda:button_click(7))
button_8 = Button(root,text=8,padx=40,pady=20,command=lambda:button_click(8))
button_9 = Button(root,text=9,padx=40,pady=20,command=lambda:button_click(9))
button_0 = Button(root,text=0,padx=40,pady=20,command=lambda:button_click(0))
button_adds = Button(root,text="+",padx=39,pady=20,command=button_add)
button_equals = Button(root,text="=",padx=91,pady=20,command=button_equals,bg="#add8e6")
button_clear = Button(root,text="Clear",padx=79,pady=20,command=button_clear,fg="red")

button_subtract = Button(root,text="-",padx=41,pady=20,command=button_subtract)
button_divide = Button(root,text="/",padx=40,pady=20,command=button_divide)
button_multiply = Button(root,text="*",padx=41,pady=20,command=button_multiply)
button_modulus = Button(root,text="%",padx=150,pady=20,command=button_modulus)
#buttons on the screens
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
button_adds.grid(row=5,column=0)

button_subtract.grid(row=6,column=0)
button_divide.grid(row=6,column=1)
button_multiply.grid(row=6,column=2)
button_modulus.grid(row=7,columnspan=3)

button_equals.grid(row=5,column=1,columnspan=2)
button_clear.grid(row=4,column=1,columnspan=2)

#looping
root.mainloop()