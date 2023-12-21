from tkinter import *
from tkinter import ttk
import socket
import threading

#UI Until 80
root = Tk()

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

# row 4,5 are free

# Requested Data - UI
ttk.Label(root, text="The Requested data:").grid(row=5, column=0)
txtRequestedData = Text(root, width=30, height=15, font=font1)
txtRequestedData.grid(row=5, column=1, columnspan=2)

# Request/Quit - UI
buRequest = ttk.Button(root, text='Request')
buRequest.grid(row=6, column=3)
buQuit = ttk.Button(root, text='Quit')
buQuit.grid(row=6, column=2)
#------FINISH OF UI-------
cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

""" def ReceiveInformationAndSendIt():
    username = username_entry.get()
    username_entry.delete(0, END)
    icao = icao_entry.get()
    icao_entry.delete(0, END)

    def network_task():
        cs.connect(("127.0.0.1", 49999))
        data, addr = cs.recvfrom(4096)
        print(f"Server >> {data.decode()}")
        cs.send(icao.encode())
        data, addr = cs.recvfrom(4096)
        print(data.decode())  # line 143 in server
        cs.send(OptionChose.get().encode('ascii'))

    network_thread = threading.Thread(target=network_task)
    network_thread.start() """

cs.connect(('127.0.0.1',12345))
username = username_entry.get()
cs.send(username.encode('ascii'))
def goodBye():
    # TODO: Quit
    print("Bye!")

""" buRequest.config(command=ReceiveInformationAndSendIt)
buQuit.config(command=goodBye) """
root.mainloop()
