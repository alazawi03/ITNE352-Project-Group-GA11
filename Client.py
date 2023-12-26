from tkinter import *
from tkinter import ttk
import socket
import time
import json

#TODO: C,D switch will lead to error 

root = Tk()#Create the GUI object
#GUI Style touches
root.title('Flight Client')
style = ttk.Style()
root.configure(background='#e1d8b2')
style.theme_use('classic')
style.configure('TLabel', background='#e1d8b2')
style.configure('TButton', background='#e1d8b2')
style.configure('TRadioButton', background='#e1d8b2')

def connect_to_server():
    while True:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_address = ('127.0.0.1', 12345)
            client.connect(server_address)
            print("Connected to the server.")
            return client
        except Exception as e:
            print(f"Connection failed: {e}")
            time.sleep(5)  # Wait for 5 seconds before retrying

client=connect_to_server()

def handle_connection(isCliked):
    
    while isCliked==True:
        isCliked=False #Will become True if Request button is clicked in GUI
        option_chose = OptionChose.get() #OptioChose() value is derived from the GUI

        if option_chose=='quit':
            destroy() 
            break #exit the loop (then the function)

        client.send(option_chose.encode('ascii')) #a or b or c or d

        #C/D need paramter from the client
        if option_chose == 'c': 
            parm = optionC_entry.get()
            time.sleep(0.5) #so do not happen error
            client.send(parm.encode('ascii'))
        elif option_chose == 'd':
            parm = optionD_entry.get()
            time.sleep(0.5) #so do not happen error
            client.send(parm.encode('ascii'))

        try:
            received_data = receive_large_data(client)
            print_as_table(json.loads(received_data), option_chose)
        except json.JSONDecodeError as e:
            print(f"JSON decoding error: {e}")

#Terminate everything
def destroy():
    client.send('quit'.encode('ascii'))
    root.destroy()
    client.close()

#The received data can be larger than socket buffer size
def receive_large_data(sock):
    BUFF_SIZE = 4096 
    data = b''
    while True:
        part = sock.recv(BUFF_SIZE)
        data += part
        if len(part) < BUFF_SIZE:
            # either 0 or end of data
            break
    return data.decode('ascii')

#print the received data into the GUI
def print_as_table(rcvData,opt):

    if opt=='a':
        table = ttk.Treeview(root, columns=(0,1,2,3,4))
        table.grid(row=5, column=1, columnspan=2)
        table.column('#0', width=0, stretch=NO) #hide the default column by tkinter library
        table.heading(0, text='flight_IATA')
        table.heading(1, text='departure_airport')
        table.heading(2, text='arrival_actual')
        table.heading(3, text='arrival_terminal')
        table.heading(4, text='arrival_gate')
        for flight in rcvData:
                frst = flight['flight_IATA'],
                scnd = flight['departure_airport'],
                thrd = flight['arrival_actual'],
                forth = flight['arrival_terminal'],
                fifth = flight['arrival_gate']
                data = (frst,scnd,thrd,forth,fifth)
                table.insert(parent = '', index = 0, values = data)


    elif opt=='b':
        table = ttk.Treeview(root, columns=(0, 1, 2, 3, 4,5,6))
        table.grid(row=5, column=1, columnspan=2)
        table.column('#0', width=0, stretch=NO) #hide the default column by tkinter library
        table.heading(0, text='flight_IATA')
        table.heading(1, text='departure_airport')
        table.heading(2, text='org_departure_time')
        table.heading(3, text='estimated_arrival_time')
        table.heading(4, text='arrival_terminal')
        table.heading(5, text='departure_delay')
        table.heading(6, text='arrival_gate')
        for flight in rcvData:
                frst = flight['flight_IATA'],
                scnd = flight['departure_airport'],
                thrd = flight['org_departure_time'],
                forth = flight['estimated_arrival_time'],
                fifth = flight['arrival_terminal']
                sixth = flight['departure_delay']
                seventh = flight['arrival_gate']
                data = (frst,scnd,thrd,forth,fifth,sixth,seventh)
                table.insert(parent = '', index = 0, values = data)


    elif opt=='c':
        table = ttk.Treeview(root, columns=(0, 1, 2, 3, 4,5,6))
        table.grid(row=5, column=1, columnspan=2)
        table.column('#0', width=0, stretch=NO) #hide the default column by tkinter library
        table.heading(0, text='flight_iata')
        table.heading(1, text='departure_airport')
        table.heading(2, text='org_departure_time')
        table.heading(3, text='estimated_arrival_time')
        table.heading(4, text='departure_gate')
        table.heading(5, text='arrival_gate')
        table.heading(6, text='status')
        for flight in rcvData:
                frst = flight['flight_iata'],
                scnd = flight['departure_airport'],
                thrd = flight['departure_time'],
                forth = flight['arrival_estimated'],
                fifth = flight['departure_gate']
                sixth = flight['arrival_gate']
                seventh = flight['status']
                data = (frst,scnd,thrd,forth,fifth,sixth,seventh)
                table.insert(parent = '', index = 0, values = data)

                
    elif opt=='d':
        table = ttk.Treeview(root, columns=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
        table.grid(row=5, column=1, columnspan=2)
        table.column('#0', width=0, stretch=NO) #hide the default column by tkinter library

        table.heading(0, text='flight_IATA')
        table.column(0, width=70)

        table.heading(1, text='departure_airport')
        table.column(1, width=180)

        table.heading(2, text='departure_gate')
        table.column(2, width=90)

        table.heading(3, text='departure_terminal')
        table.column(3, width=120, stretch=YES)

        table.heading(4, text='arrival_airport')
        table.column(4, width=120, stretch=YES)

        table.heading(5, text='arrival_gate')
        table.column(5, width=70)

        table.heading(6, text='arrival_terminal')
        table.column(6, width=90)

        table.heading(7, text='status')
        table.column(7, width=70)

        table.heading(8, text='departure_scheduled')
        table.column(8, width=150)

        table.heading(9, text='arrival_scheduled')
        table.column(9, width=150)
        for flight in rcvData:
                frst = flight['flight_IATA'],
                scnd = flight['departure_airport'],
                thrd = flight['departure_gate'],
                forth = flight['departure_terminal'],
                fifth = flight['arrival_airport']
                sixth = flight['arrival_gate']
                seventh = flight['arrival_terminal']
                eight = flight['status']
                nine = flight['departure_scheduled']
                ten = flight['arrival_scheduled']
                data = (frst,scnd,thrd,forth,fifth,sixth,seventh,eight,nine,ten)
                table.insert(parent = '', index = 0, values = data)

#The username will be asked first
username_label = ttk.Label(root, text='Username: ')
username_label.grid(row=0, column=0)
username_entry = ttk.Entry(root)
username_entry.grid(row=0, column=1, columnspan=2)
def connect_first_time():
    #Retrive the username from the input in GUI and send it
    username = username_entry.get()
    client.send(username.encode('ascii'))

    #Hide all the username widgets
    buConnect.grid_forget()
    username_entry.grid_forget()
    username_label.grid_forget()

    #Show all widgets of requesting in the GUI
    askToChoose.grid(row=2, column=0)
    buRequest.grid(row=6, column=3)
    rb1.grid(row=2, column=1)
    rb2.grid(row=2, column=2)
    rb3.grid(row=3, column=1)
    rb4.grid(row=3, column=2)
buConnect = ttk.Button(root, text='Connect', command=connect_first_time)
buConnect.grid(row=1, column=1, columnspan=2)

#The following lines is creation to allow client to send the extra paramters for option C/D
#They will be hidden untill the option is chosen
optionC_label = ttk.Label(root, text='Enter departure IATA: ')
optionC_label.grid(row=4, column=1)
optionC_entry = ttk.Entry(root)
optionC_entry.grid(row=4, column=2)
optionC_label.grid_remove()
optionC_entry.grid_remove()

optionD_label = ttk.Label(root, text='Enter Flight IATA: ')
optionD_label.grid(row=4, column=1)
optionD_entry = ttk.Entry(root)
optionD_entry.grid(row=4, column=2)
optionD_label.grid_remove() 
optionD_entry.grid_remove()

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

# Choose Option -- a/b/c/d (GUI)
OptionChose = StringVar()
askToChoose = ttk.Label(root, text='Please choose an Option To request')
rb1 = ttk.Radiobutton(root, text='A. Arrived Flights', variable=OptionChose, value='a', command=toggle_entry_state)
rb2 = ttk.Radiobutton(root, text='B. Delayed Flights', variable=OptionChose, value='b', command=toggle_entry_state)
rb3 = ttk.Radiobutton(root, text='C. Flights from Specific City', variable=OptionChose, value='c', command=toggle_entry_state)
rb4 = ttk.Radiobutton(root, text='D. Details of a Particular Flight', variable=OptionChose, value='d', command=toggle_entry_state)

# Request/Quit Buttons (GUI)
buRequest = ttk.Button(root, text='Request', command=lambda: handle_connection(True))
buQuit = ttk.Button(root, text='Quit', command=destroy) 
buQuit.grid(row=6, column=2)

root.mainloop()