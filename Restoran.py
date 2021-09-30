import tkinter
from tkinter.constants import W, X, Y
import tkinter.messagebox
import typing_extensions
import numpy
from math import sqrt,ceil

window = tkinter.Tk()

window.title("Menu")
Array =[]

Meni = ["Pizza", "Burger", "Caesar salad", "Lasagne",
        "Ham sandwich", "Omelette", "Pasta", "Pancakes","Popcorn","Sweets"]
        
Cijene = [3.50, 3.50, 4.00, 5.00, 2.00, 3.00, 5.50, 2.33,1.4,6.5]

Spojeno = ['%.2f' % trag for trag in Cijene]

Ponisti = [tkinter.IntVar() for m in Meni]  

def reset():
    for i in range(len(Array)):
       Ponisti[i].set(0)

i = 0

while i != len(Spojeno):
    Meni[i] = Meni[i]+"(" + Spojeno[i] + ")"
    i =i+ 1

j = 0
x = 0  #R
y = 0  #C

duzinaKolone = ceil(sqrt(len(Meni)/2)) 
duzinaReda = duzinaKolone * 2

#2:1

while x != duzinaReda :
    y=0
    while y != duzinaKolone and j != len(Meni):
        items = tkinter.Checkbutton(window, text=Meni[j], onvalue=1, offvalue=0,variable=Ponisti[j]) 
        Array.append(items)
        items.grid(row=x, column=y, sticky=W)
        y = y+1
        j = j+1
    x=x+1
        

    

#Sum Fun
def sum():
    sum = 0
    for i, var in enumerate(Ponisti):
        sum = sum + var.get() * Cijene[i] 
    return format(sum,'.2f')

def order():
    
    tkinter.messagebox.showinfo("Message","Your order is successful.The total amount is:" + " " + str(sum()))

frame1 = tkinter.Frame(window,height=100,width=100)
frame1.grid(row=x,columnspan=duzinaKolone)

orderdugme = tkinter.Button(frame1,text="Order",command=order)
orderdugme.pack(side="left")

canceldugme = tkinter.Button(frame1,text="Cancel",command=reset)
canceldugme.pack(side="right")

window.mainloop()