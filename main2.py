# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 11:33:55 2019

@author: Akhil
"""
import tkinter as tk
from tkinter import *
import gui
window = tk.Tk()
window.title("Twitter Sentiment Analysis App")
#window.geometry('480x270')
lbl=tk.Label (window,text="Twitter Sentiment Analysis",font=("Arial Bold", 10))
lbl.grid(column=0,row=0)
#lbl2=tk.Label(window,text="\n")
#lbl2.grid(column=0,row=1)
lbl3=tk.Label(window,text="Enter hashtag:")
lbl3.grid(column=0,row=1)
lbl4=tk.Label(window,text="")
lbl4.grid(column=0,row=6)
lbl5=tk.Label(window,text="")
lbl5.grid(column=0,row=7)
lbl6=tk.Label(window,text="")
lbl6.grid(column=0,row=8)
txt=tk.Entry(window)
txt.grid(column=0,row=2)
def clicked():
    store=""+txt.get()
    pos=gui.calculate(store)
    neg=100-pos
    pos="Postive Sentiment: "+str(pos)+" %"
    neg="Negative Sentiment: "+str(neg)+" %"
    lbl5.configure(text=pos)
    lbl6.configure(text=neg)
def clear():
    lbl5.configure(text="")
    lbl6.configure(text="")
    
btn = tk.Button(window, text="Analyse",bg="white",fg="blue",command=clicked) 
btn.grid(column=0, row=4)
btn2 = tk.Button(window, text="Clear",bg="white",fg="blue",command=clear) 
btn2.grid(column=0, row=5)
#store=txt.get()
#lbl4=tk.Label(window,text=store)
window.mainloop()
