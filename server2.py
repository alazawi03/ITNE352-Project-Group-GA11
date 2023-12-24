import requests
import json
import socket
import threading

#TODO: ERROR HANDEL
#TODO: 
'''
#1. Ask the user to enter arr_icao
arr_icao=input("Please enter airport code: ")

#2. Retrive 100 records of flight at the specefied airport
API_ACCESS_KEY = "ec9a339729e37e6f9dcb2531ca197d4e"
API_ENDPOINT = "http://api.aviationstack.com/v1/flights"
RECORDS=100
request_params = {
    'access_key': API_ACCESS_KEY,
    'arr_icao': arr_icao,
    'limit': RECORDS  
}
response = requests.get(API_ENDPOINT, params=request_params)
data = response.json()

#3. Store the retrived data in JSON file caleed "group_ID.json"
with open('GA11.json','w') as f:
    json.dump(data, f, indent=2)
    print("File saved") #TODO: better message
'''

#4. Wait for client requests to connect (at least 3 connections)

def retriveData(option,parm):
   with open('GA11.json','r') as rf:
    data=json.load(rf)['data']
    if option=='a':
        temp=[]
        r=0
        for i in data:
            if i['flight_status']=='landed':
                r+=1
                d={
                    'flight_IATA':i['flight']['iata'],
                    'departure_airport':i['departure']['airport'],
                    'arrival_actual':i['arrival']['actual'],
                    'arrival_terminal':i['arrival']['terminal'],
                    'arrival_gate':i['arrival']['gate']
                }
                temp.append(d)
        return temp,r
    elif option=='b':
        temp=[]
        r=0
        for i in data:
            if i['departure']['delay'] != None:
                r+=1
                d={
                    'flight_IATA':i['flight']['iata'],
                    'departure_airport':i['departure']['airport'],
                    'org_departure_time"':i['arrival']['scheduled'],
                    'estimated_arrival_time"':i['arrival']['estimated'],
                    'arrival_terminal':i['arrival']['terminal'],
                    'departure_delay':i['departure']['delay'],
                    'arrival_gate':i['arrival']['gate']
                }
                temp.append(d)
        return temp,r
    elif option=='c':
        temp=[]
        r=0
        for i in data:
            if i['departure']['iata'] == parm:
                r+=1
                d={
                    'flight_iata':i['flight']['iata'],
                    'departure_airport':i['departure']['airport'],
                    'departure_time':i['departure']['actual'],
                    'arrival_estimated':i['arrival']['estimated'],
                    'departure_gate':i['departure']['gate'],
                    'arriva;_gate':i['arrival']['gate'],
                    'status':i['flight_status']
                }
                temp.append(d)
        return temp,r
    elif option=='d':
        temp=[]
        r=0
        for i in data:
            if i['flight']['number'] == parm:
                r+=1
                d={
                    'flight_IATA':i['flight']['iata'],
                    'departure_airport':i['departure']['airport'],
                    'departure_gate':i['departure']['gate'],
                    'departure_terminal':i['departure']['terminal'],
                    'arrival_airport':i['arrival']['airport'],
                    'arrival_gate':i['arrival']['gate'],
                    'arrival_terminal':i['arrival']['terminal'],
                    'status':i['flight_status'],
                    'departure_scheduled':i['departure']['scheduled'],
                    'arrival_scheduled':i['arrival']['scheduled']
                }
                temp.append(d)
                return temp,r #it is only one flight, no need to waste more time,process
    return "Not Found","0"
       
def opt(option):
    parm="-1"
    option_disp=""
    if option=='a':
        option_disp="A. Arrived Flights"
    elif option=='b':
        option_disp="B. Delayed Flights"
    elif option=='c':
        parm=client_socket.recv(1024).decode('ascii')
        option_disp=f"C. Flights from Specific City with departure IATA {parm}"
    elif option=='d':
        parm=client_socket.recv(1024).decode('ascii')
        option_disp=f"D. Details of a Particular Flight with flight number {parm}"
    else:
        print(f"Not found, \n\n {option}")
    return option_disp,parm

def handle_client(client_socket,name,counter):
    while True:
        option = client_socket.recv(1024).decode('ascii')
        print("\n\n", 25*"*","\n\n" )
        print(option)
        print("\n\n", 25*"*","\n\n" )
        if option=='quit':
            print(f"{name} has been discconnected")
            client_socket.close()
            return
        option_disp,parm=opt(option=option)
  

        print(f"{counter}. {name} >> asks for {option_disp} ")
        data,no_of_records=retriveData(option=option,parm=parm)
        print("\n\n", 25*"*","\n\n" )
        print(data)
        print(no_of_records)
        print("\n\n", 25*"*","\n\n" )

        if data=='Not Found' and no_of_records=='0':
            msg = "Error 404 Not Found"
            client_socket.send(msg.encode('ascii'))
        else:
            #send Number of records
            client_socket.send(str(no_of_records).encode('ascii'))

            # Send the list to the client
            response = json.dumps(data, indent=2)
            print(response) # FOR TESTING
            client_socket.send(response.encode('ascii'))

addres=('127.0.0.1',12345) 
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(addres)
server.listen(5) #at least 3, can be 5
print(f"Server listening on {addres}")

counter=0
while True:
    counter+=1
    client_socket, addr = server.accept()
    client_name = client_socket.recv(1024)
    name=client_name.decode('ascii')
    if name=='quit':
        client_socket.close()
        continue
    print(f"Accepted Connection No.{counter} with {name}")
    client_handler= threading.Thread(target=handle_client, args=(client_socket,name,counter))
    client_handler.start()