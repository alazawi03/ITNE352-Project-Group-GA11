import requests
import json
import socket
import threading

saved=True
#Ask the user to enter arr_icao
arr_icao=input("Please enter airport code: ")

 #Retrive 100 records of flight at the specefied airport
API_ACCESS_KEY = "38a43965725826968ae9be37e1d6a69f"
API_ENDPOINT = "http://api.aviationstack.com/v1/flights"
RECORDS=100
request_params = {
    'access_key': API_ACCESS_KEY,
    'arr_icao': arr_icao,
    'limit': RECORDS  
}

try:
    api_result = requests.get(API_ENDPOINT, params=request_params)

    # Check if the API request was successful (status code 200)
    api_result.raise_for_status()

    # Process the API response here
    data = api_result.json()
    with open('GA11.json', 'w') as f:
        json.dump(data, f, indent=2)
        print(f"Server >> {arr_icao} airport data was saved into storage")

except requests.exceptions.RequestException as e:
    # Handle exceptions related to making API requests
    print(f"Error making API request: {e}  \nPlease Fix the error and restart the server.")
    saved=False

except json.JSONDecodeError as e:
    # Handle JSON decoding errors
    print(f"Error decoding JSON: {e}  \nPlease Fix the error and restart the server.")
    saved=False

except Exception as e:
    # Handle other unexpected exceptions
    print(f"\nAn unexpected error occurred: {e}  \nPlease Fix the error and restart the server.")
    saved=False

#This function {retriveData} will be called to cache the data before sending it to the client  """
def retriveData(option,parm):
   with open('GA11.json','r') as rf:
    data=json.load(rf)['data']
    if option=='a':
        temp=[]
        for i in data:
            if i['flight_status']=='landed':
                tempFlight={
                    'flight_IATA':i['flight']['iata'],
                    'departure_airport':i['departure']['airport'],
                    'arrival_actual':i['arrival']['actual'],
                    'arrival_terminal':i['arrival']['terminal'],
                    'arrival_gate':i['arrival']['gate']
                }
                temp.append(tempFlight)
        return temp
    
    elif option=='b':
        temp=[]
        for i in data:
            if i['arrival']['delay'] != None:
                tempFlight={
                    'flight_IATA':i['flight']['iata'],
                    'departure_airport':i['departure']['airport'],
                    'org_departure_time':i['departure']['actual'],
                    'estimated_arrival_time':i['arrival']['estimated'],
                    'arrival_terminal':i['arrival']['terminal'],
                    'departure_delay':i['departure']['delay'],
                    'arrival_gate':i['arrival']['gate']
                }
                temp.append(tempFlight)
        return temp
    
    elif option=='c':
        temp=[]
        for i in data:
            if i['departure']['iata'] == parm:
                tempFlight={
                    'flight_iata':i['flight']['iata'],
                    'departure_airport':i['departure']['airport'],
                    'departure_time':i['departure']['actual'],
                    'arrival_estimated':i['arrival']['estimated'],
                    'departure_gate':i['departure']['gate'],
                    'arrival_gate':i['arrival']['gate'],
                    'status':i['flight_status']
                }
                temp.append(tempFlight)
        return temp
    
    else: #option d
        temp=[]
        for i in data:
            if i['flight']['iata'] == parm:
                tempFlight={
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
                temp.append(tempFlight)
        return temp 

#This function is just used to format the message to print it
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

    return option_disp,parm

def handle_client(client_socket,name,counter):
    while True:
        try:
            option = client_socket.recv(1024).decode('ascii') #a/b/c/d or quit will be received from the client
        
            if option=='quit':   #quit case
                print(f"{counter}. {name} >> has been discconnected")
                client_socket.close()
                return
            
            option_disp,parm=opt(option=option) #format the option to print it
            print(f"{counter}. {name} >> asks for {option_disp} ")
            data=retriveData(option=option,parm=parm) #Retrieve the data from the json file stoerd 
            client_socket.send(json.dumps(data, indent=2).encode('ascii'))
        except (ConnectionAbortedError or ConnectionResetError):
            print(f"{counter}. {name} >> connection aborted; disconnected...")
            client_socket.close()
            break
        

if saved:
    #Wait for client requests to connect (at least 3 connections)
    addres=('127.0.0.1',12345) 
    server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(addres)
    server.listen(3)
    print(f"Server listening on {addres}")
    print(2*"\n"," ✈️ "*7," Welcome to Server"," ✈️ "*7,2*"\n")
    counter=0 #Count the connections in the server
    while True:   
        try:
            client_socket, addr = server.accept()
            counter+=1 
            client_name = client_socket.recv(1024)
            name=client_name.decode('ascii')
            if name=='quit': #in case the client quit before putting his name
                client_socket.close()
                continue
            print(f"Accepted Connection No.{counter} with {name}")
            #Each client will have 
            client_handler= threading.Thread(target=handle_client, args=(client_socket,name,counter))
            client_handler.start()
        except (KeyboardInterrupt):
            print(f"{name} error... keyboard Interrupt")
        


        