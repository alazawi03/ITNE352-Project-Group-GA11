from tkinter import *
from tkinter import ttk
import socket

root=Tk()
cs=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#style - UI
root.title("Flight Client")
style=ttk.Style()
root.configure(background='#e1d8b2')
style.theme_use('classic')
style.configure('TLabel',background='#e1d8b2')
style.configure('TButton',background='#e1d8b2')
style.configure('TRadioButton',background='#e1d8b2')
font1=('Arial',16)

#Username - UI
username_label=ttk.Label(root, text="Username: ")
username_label.grid(row=0, column=0)
username_entry=ttk.Entry(root)
username_entry.grid(row=0, column=1, columnspan=2)

#Choose Option - UI
askToChoose=ttk.Label(root, text="Please choose an Option To request")
askToChoose.grid(row=1,column=0)
rb1=ttk.Radiobutton(root,text='A. Arrived Flights')
rb1.grid(row=1, column=1)
rb2=ttk.Radiobutton(root,text='B. Delayed Flights')
rb2.grid(row=1, column=2)
rb3=ttk.Radiobutton(root,text='C. Flights from Specific City')
rb3.grid(row=2, column=1)
rb4=ttk.Radiobutton(root,text='D. Details of a Particular Flight')
rb4.grid(row=2, column=2)

#Requested Data - UI
ttk.Label(root,text="The Requested data:").grid(row=2, column=0)
txtRequestedData=Text(root, width=30, height=15, font=font1)
txtRequestedData.grid(row=3, column=1, columnspan=2)

#Request/Quit - UI
buRequest=ttk.Button(root,text='Request')
buRequest.grid(row=8, column=3)
buQuit=ttk.Button(root,text='Quit')
buQuit.grid(row=8, column=2)
root.mainloop()