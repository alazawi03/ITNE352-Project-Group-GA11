from tkinter import *
from tkinter import ttk
import socket
import time
import json


client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',12345))

def receive_large_data(sock):
    BUFF_SIZE = 4096 # 4 KiB
    data = b''
    while True:
        part = sock.recv(BUFF_SIZE)
        data += part
        if len(part) < BUFF_SIZE:
            # either 0 or end of data
            break
    return data

def print_as_table(js,opt):
    if opt=='a':
        table = ttk.Treeview(root, columns=(0, 1, 2, 3, 4))
        table.grid(row=5, column=1, columnspan=2)
        table.column('#0', width=0, stretch=NO) #hide the default column by tkinter library
        table.heading(0, text="flight_IATA")
        table.heading(1, text="departure_airport")
        table.heading(2, text="arrival_actual")
        table.heading(3, text="arrival_terminal")
        table.heading(4, text="arrival_gate")
        for flight in js:
                frst = flight["flight_IATA"],
                scnd = flight["departure_airport"],
                thrd = flight["arrival_actual"],
                forth = flight["arrival_terminal"],
                fifth = flight["arrival_gate"]
                data = (frst,scnd,thrd,forth,fifth)
                table.insert(parent = '', index = 0, values = data)
    elif opt=='b':
        table = ttk.Treeview(root, columns=(0, 1, 2, 3, 4,5,6))
        table.grid(row=5, column=1, columnspan=2)
        table.column('#0', width=0, stretch=NO) #hide the default column by tkinter library
        table.heading(0, text="flight_IATA")
        table.heading(1, text="departure_airport")
        table.heading(2, text="org_departure_time")
        table.heading(3, text="estimated_arrival_time")
        table.heading(4, text="arrival_terminal")
        table.heading(5, text="departure_delay")
        table.heading(6, text="arrival_gate")
        for flight in js:
                frst = flight["flight_IATA"],
                scnd = flight["departure_airport"],
                thrd = flight["org_departure_time"],
                forth = flight["estimated_arrival_time"],
                fifth = flight["arrival_terminal"]
                sixth = flight["departure_delay"]
                seventh = flight["arrival_gate"]
                data = (frst,scnd,thrd,forth,fifth,sixth,seventh)
                table.insert(parent = '', index = 0, values = data)
    elif opt=='c':
        table = ttk.Treeview(root, columns=(0, 1, 2, 3, 4,5,6))
        table.grid(row=5, column=1, columnspan=2)
        table.column('#0', width=0, stretch=NO) #hide the default column by tkinter library
        table.heading(0, text="flight_iata")
        table.heading(1, text="departure_airport")
        table.heading(2, text="org_departure_time")
        table.heading(3, text="estimated_arrival_time")
        table.heading(4, text="departure_gate")
        table.heading(5, text="arrival_gate")
        table.heading(6, text="status")
        for flight in js:
                frst = flight["flight_iata"],
                scnd = flight["departure_airport"],
                thrd = flight["departure_time"],
                forth = flight["arrival_estimated"],
                fifth = flight["departure_gate"]
                sixth = flight["arrival_gate"]
                seventh = flight["status"]
                data = (frst,scnd,thrd,forth,fifth,sixth,seventh)
                table.insert(parent = '', index = 0, values = data)
    elif opt=='d':
        table = ttk.Treeview(root, columns=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
        table.grid(row=5, column=1, columnspan=2)
        table.column('#0', width=0, stretch=NO) #hide the default column by tkinter library

        table.heading(0, text="flight_IATA")
        table.column(0, width=70)

        table.heading(1, text="departure_airport")
        table.column(1, width=180)

        table.heading(2, text="departure_gate")
        table.column(2, width=90)

        table.heading(3, text="departure_terminal")
        table.column(3, width=120, stretch=YES)

        table.heading(4, text="arrival_airport")
        table.column(4, width=120, stretch=YES)

        table.heading(5, text="arrival_gate")
        table.column(5, width=70)

        table.heading(6, text="arrival_terminal")
        table.column(6, width=90)

        table.heading(7, text="status")
        table.column(7, width=70)

        table.heading(8, text="departure_scheduled")
        table.column(8, width=150)

        table.heading(9, text="arrival_scheduled")
        table.column(9, width=150)
        for flight in js:
                frst = flight["flight_IATA"],
                scnd = flight["departure_airport"],
                thrd = flight["departure_gate"],
                forth = flight["departure_terminal"],
                fifth = flight["arrival_airport"]
                sixth = flight["arrival_gate"]
                seventh = flight["arrival_terminal"]
                eight = flight["status"]
                nine = flight["departure_scheduled"]
                ten = flight["arrival_scheduled"]
                data = (frst,scnd,thrd,forth,fifth,sixth,seventh,eight,nine,ten)
                table.insert(parent = '', index = 0, values = data)

    

def destroy():
    client.send('quit'.encode('ascii'))
    root.destroy()
    client.close()

def connect_first_time():
    buConnect.grid_forget()
    username = username_entry.get()
    username_entry.grid_forget()
    username_label.grid_forget()
    client.send(username.encode('ascii'))
    askToChoose.grid(row=2, column=0)
    buRequest.grid(row=6, column=3)
    rb1.grid(row=2, column=1)
    rb2.grid(row=2, column=2)
    rb3.grid(row=3, column=1)
    rb4.grid(row=3, column=2)
    #TODO: print connection has been established

def requestClicked():
        cs(True)

def cs(isCliked):
    while isCliked==True:
        isCliked=False
        option_chose = OptionChose.get()
        if option_chose=='quit':
            destroy()
            break
        client.send(option_chose.encode('ascii'))
        if option_chose == 'c':
            parm = optionC_entry.get()
            time.sleep(0.5) #so do not happen error
            client.send(parm.encode('ascii'))
        elif option_chose == 'd':
            parm = optionD_entry.get()
            time.sleep(0.5) #so do not happen error
            client.send(parm.encode('ascii'))
        number_of_records=client.recv(4096).decode('ascii')
        if number_of_records=='Error 404 Not Found':
            #TODO: Display Error,..
            print('ERROR')
        else:
            received_data = receive_large_data(client)
            received_data=received_data.decode('ascii')
            print(json.loads(received_data))
            print_as_table(json.loads(received_data),option_chose)
            
            
    
        
    
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
    OptionChose.set('quit')
    cs()


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

OptionChose = StringVar()

rb1 = ttk.Radiobutton(root, text='A. Arrived Flights', variable=OptionChose, value="a", command=toggle_entry_state)
rb2 = ttk.Radiobutton(root, text='B. Delayed Flights', variable=OptionChose, value="b", command=toggle_entry_state)
rb3 = ttk.Radiobutton(root, text='C. Flights from Specific City', variable=OptionChose, value="c", command=toggle_entry_state)
rb4 = ttk.Radiobutton(root, text='D. Details of a Particular Flight', variable=OptionChose, value="d", command=toggle_entry_state)

# Request/Quit - UI
buRequest = ttk.Button(root, text='Request', command=requestClicked)



buQuit = ttk.Button(root, text='Quit', command=destroy) 
buQuit.grid(row=6, column=2)

buConnect = ttk.Button(root, text='Connect', command=connect_first_time)
buConnect.grid(row=1, column=1, columnspan=2)


root.mainloop()