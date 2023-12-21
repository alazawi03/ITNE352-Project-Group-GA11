from tkinter import *
from tkinter import ttk, simpledialog
import socket
import threading

#CLIENT

""" client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',12345)) """

def cs():
    username = username_entry.get()
    client.send(username.encode('ascii'))
    option_chose = OptionChose.get()
    client.send(option_chose.encode('ascii'))
    if option_chose == 'c' or option_chose == 'd':
        parm = optionC_entry.get()
        client.send(parm.encode('ascii'))

def toggle_entry_state():
    optionC_label.grid_remove()
    optionC_entry.grid_remove()
    optionD_label.grid_remove()
    optionD_entry.grid_remove()
    if OptionChose.get() == 'c':
        optionC_label.grid()
        optionC_entry.grid()
    elif OptionChose.get() == 'd':
        optionD_label.grid()
        optionD_entry.grid()

def quit_and_change_option():
    client.send("quit".encode('ascii'))
    root.destroy()
    client.close()

#START UI
root = Tk()
# option C
optionC_label = ttk.Label(root, text="Enter departure IATA: ")
optionC_label.grid(row=4, column=1)
optionC_entry = ttk.Entry(root)
optionC_entry.grid(row=4, column=2)
optionC_label.grid_remove()
optionC_entry.grid_remove()

# option D
optionD_label = ttk.Label(root, text="Enter Flight Number: ")
optionD_label.grid(row=4, column=1)
optionD_entry = ttk.Entry(root)
optionD_entry.grid(row=4, column=2)
optionD_label.grid_remove()
optionD_entry.grid_remove()

# style - UI
root.title("Flight Client")
style = ttk.Style()
root.configure(background='#e1d8b2')
style.theme_use('classic')
style.configure('TLabel', background='#e1d8b2')
style.configure('TButton', background='#e1d8b2')
style.configure('TRadioButton', background='#e1d8b2')
font1 = ('Arial', 16)

# Username - UI
username_label = ttk.Label(root, text="Username: ")
username_label.grid(row=0, column=0)
username_entry = ttk.Entry(root)
username_entry.grid(row=0, column=1, columnspan=2)

# Choose Option - UI
askToChoose = ttk.Label(root, text="Please choose an Option To request")
askToChoose.grid(row=2, column=0)
OptionChose = StringVar()
rb1 = ttk.Radiobutton(root, text='A. Arrived Flights', variable=OptionChose, value="a", command=toggle_entry_state)
rb1.grid(row=2, column=1)
rb2 = ttk.Radiobutton(root, text='B. Delayed Flights', variable=OptionChose, value="b", command=toggle_entry_state)
rb2.grid(row=2, column=2)
rb3 = ttk.Radiobutton(root, text='C. Flights from Specific City', variable=OptionChose, value="c", command=toggle_entry_state)
rb3.grid(row=3, column=1)
rb4 = ttk.Radiobutton(root, text='D. Details of a Particular Flight', variable=OptionChose, value="d", command=toggle_entry_state)
rb4.grid(row=3, column=2)


# Requested Data - UI
ttk.Label(root, text="The Requested data:").grid(row=5, column=0)
txtRequestedData = Text(root, width=30, height=15, font=font1)
txtRequestedData.grid(row=5, column=1, columnspan=2)

# Request/Quit - UI
buRequest = ttk.Button(root, text='Request', command=cs)
buRequest.grid(row=6, column=3)
buQuit = ttk.Button(root, text='Quit', command=quit_and_change_option)
buQuit.grid(row=6, column=2)


root.mainloop()