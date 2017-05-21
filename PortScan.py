#!/usr/bin/python2.7
# -*- coding:utf-8 -*-
#By DoJoker
#PortScan

from Tkinter import *
import PortScan

ports=[21,22,23,80,1433,3389,8080]
def tgtScan(host)
	PortScan.
def btn_click():
	tgthost = input_host.get()
	portScan(tgthost)	
root = Tk()
root.title('PortScan')
input_host = Entry(root, text = 'input host')
input_host.pack()
scan = Button(root,text='Scan',command=btn_click)
scan['width'] = 5
scan['height'] = 1
scan.pack()

root.mainloop()