from tkinter import *
from tkinter import ttk, messagebox
import socket
import time
import json

root = Tk()#Create the GUI object
table = ttk.Treeview(root, columns=(0,1,2,3,4,5,6,7,8,9)) #Identified it here, so i can use it inside below functions

#GUI Style touches
root.title('Flight Client')
style = ttk.Style()
root.configure(background='#e1d8b2')
style.theme_use('classic')
style.configure('TLabel', background='#e1d8b2')
style.configure('TButton', background='#e1d8b2')
style.configure('TRadioButton', background='#e1d8b2')

#will not stop trying until connect
def connect_to_server():
    while True:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_address = ('127.0.0.1', 12345)
            client.connect(server_address)
            print("Connected to the server.")
            return client
        except Exception as e:
            print(f"Connection failed, retrying again after 5 seconds")
            time.sleep(5)  # Wait for 5 seconds before retrying

client=connect_to_server()

def handle_connection():
        option_chose = OptionChose.get() #OptioChose() value is derived from the GUI

        if option_chose=='quit':
            destroy() 
            return #exit the function

        client.send(option_chose.encode('ascii')) #a or b or c or d

        #C/D need paramter from the client
        if option_chose == 'c': 
            parm = optionC_entry.get().upper()
            time.sleep(0.5) #If not, an error can happen where option parm is sent before option chose, which is not what expected by the server 
            client.send(parm.encode('ascii'))
        elif option_chose == 'd':
            parm = optionD_entry.get().upper()
            time.sleep(0.5) #If not, an error can happen where option parm is sent before option chose, which is not what expected by the server 
            client.send(parm.encode('ascii'))

        try:
            received_data = receive_large_data(client) #use function to receive large data
        
            table.delete(*table.get_children()) #To preparte for new insertion

            print_as_table(json.loads(received_data), option_chose)

            if received_data == '[]':
                    messagebox.showinfo("Message", "There is no data for what you requested.")


        except json.JSONDecodeError as e:
            print(f"JSON decoding error: {e}")
        except Exception as e:
            # Handle other unexpected exceptions
            print(f"\nAn unexpected error occurred: {e}  \nPlease Fix the error and restart the server.")

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
table.column('#0', width=0, stretch=NO) #hide the default column by tkinter library

def print_as_table(rcvData,opt):
    table.grid(row=7 , column= 0 , columnspan= 3)

    if opt=='a':
        table.heading(0, text='Flight IATA')
        table.heading(1, text='Departure Airport')
        table.heading(2, text='Arrival Actual')
        table.heading(3, text='Arrival Terminal')
        table.heading(4, text='Arrival Gate')
        column_width=[70, 110, 135, 100, 100, 70]

        for i in range(0,5):
            table.column(i, width=column_width[i])

        for flight in rcvData:
                frst = flight['flight_IATA'],
                scnd = flight['departure_airport'],
                thrd = flight['arrival_actual'],
                forth = flight['arrival_terminal'],
                fifth = flight['arrival_gate']
                data = (frst,scnd,thrd,forth,fifth)
                table.insert(parent = '', index = 0, values = data)
        for i in range(5,10):
             table.column(i, width=0, stretch=NO) 
    elif opt=='b':
        table.heading(0, text='Flight IATA')
        table.heading(1, text='Departuer Airport')
        table.heading(2, text='Original Departure Time')
        table.heading(3, text='Estimated Arrival Time')
        table.heading(4, text='Arrival Terminal')
        table.heading(5, text='Departure Delay')
        table.heading(6, text='Arrival Gate')
        column_width=[100, 125, 155, 155, 130, 110, 90]
        for i in range(0,7):
            table.column(i, width=column_width[i])
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
        for i in range(7,10):
             table.column(i, width=0, stretch=NO) 

    elif opt=='c':
        table.heading(0, text='Flight IATA')
        table.heading(1, text='Departrure Airport')
        table.heading(2, text='Original Departure Time')
        table.heading(3, text='Estimated Arrival Time')
        table.heading(4, text='Departure Gate')
        table.heading(5, text='Arrival Gate')
        table.heading(6, text='Flight')
        column_width=[70, 110, 135, 135, 90, 110, 70]
        for i in range(0,7):
            table.column(i, width=column_width[i])
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
        for i in range(7,10):
             table.column(i, width=0, stretch=NO) 
        

                
    else: #option d
        table.heading(0, text='Flight IATA')
        table.heading(1, text='Departrure Airport')
        table.heading(2, text='Departure Gate')
        table.heading(3, text='Departure Terminal')
        table.heading(4, text='Arrival Airport')
        table.heading(5, text='Arrival Gate')
        table.heading(6, text='Arrival Terminal')
        table.heading(7, text='Flight Status')
        table.heading(8, text='Departure Scheduled')
        table.heading(9, text='Arrival Scheduled')
        column_width=[70, 110, 110, 135, 90, 90, 90, 100, 115, 100]
        for i in range(0,10):
            table.column(i, width=column_width[i])
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
   
    buRequest.grid(row=6, column=1)
    rb1.grid(row=2, column=0)
    rb2.grid(row=2, column=1)
    rb3.grid(row=3, column=0)
    rb4.grid(row=3, column=1)

buConnect = ttk.Button(root, text='Connect', command=connect_first_time)
buConnect.grid(row=6, column=1, columnspan=2)

#The following lines is creation to allow client to send the extra paramters for option C/D
#They will be hidden untill the option is chosen
optionC_label = ttk.Label(root, text='Enter departure IATA: ')
optionC_label.grid(row=4, column=0)
optionC_entry = ttk.Entry(root)
optionC_entry.grid(row=4, column=1)
optionC_label.grid_remove()
optionC_entry.grid_remove()

optionD_label = ttk.Label(root, text='Enter Flight IATA: ')
optionD_label.grid(row=4, column=1)
optionD_entry = ttk.Entry(root)
optionD_entry.grid(row=4, column=2)
optionD_label.grid_remove() 
optionD_entry.grid_remove()

def toggle_entry_state():
    buRequest.config(state = 'normal')
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
rb1 = ttk.Radiobutton(root, text='A. Arrived Flights', variable=OptionChose, value='a', command=toggle_entry_state)
rb2 = ttk.Radiobutton(root, text='B. Delayed Flights', variable=OptionChose, value='b', command=toggle_entry_state)
rb3 = ttk.Radiobutton(root, text='C. Flights from Specific City', variable=OptionChose, value='c', command=toggle_entry_state)
rb4 = ttk.Radiobutton(root, text='D. Details of a Particular Flight', variable=OptionChose, value='d', command=toggle_entry_state)

# Request/Quit Buttons (GUI)
buRequest = ttk.Button(root, text='Request', command=handle_connection)
buRequest.config(state = 'disabled') #until some radio button is chosen

buQuit = ttk.Button(root, text='Quit', command=destroy) 
buQuit.grid(row=6, column=0)

try:
    root.mainloop()
except KeyboardInterrupt:
    print("Received Ctrl+C. Cleaning")
    client.close()