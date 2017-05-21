# -*- coding: utf-8 -*-  
from Tkinter import *  
  
root = Tk()  
v = StringVar()  
v.set('000')  
for i in range(10):  
    Message(root, text='A', textvariable=v).pack()  

print(v.get())  
  

for i in [LEFT, RIGHT, CENTER]:  
    Message(root, text='ABC DEF GHI', justify=i).pack()  
 
root.mainloop()  