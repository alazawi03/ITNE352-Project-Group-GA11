import requests
import json
import socket
import threading

""" #1. Ask the user to enter arr_icao
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
 """
#4. Wait for client requests to connect (at least 3 connections)
def opt(option):
    parm="-1"
    option_disp=""
    if option=='a':
        option_disp="A. Arrived Flights"
    elif option=='b':
        option_disp="B. Delayed Flights"
    elif option=='c':
        parm=client_socket.recv(1024)
        option_disp=f"C. Flights from Specific City with departure IATA {parm}"
    elif option=='d':
        parm=client_socket.recv(1024)
        option_disp=f"D. Details of a Particular Flight with flight number {parm}"
    elif option=='quit':
        option_disp="Quiting..."
    return parm,option_disp

def handle_client(client_socket,name):
    option = client_socket.recv(1024)
    option=option.decode('ascii')
    option_disp,parm=opt(option=option)
    print(f"{name}>> asks for {option_disp}")
    
    
    #client_socket.send(response)
    #client_socket.close()

addres=('127.0.0.1',12345) 
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(addres)
server.listen(5)
print(f"Server listening on {addres}")

counter=0
while True:
    counter+=1
    client_socket, addr = server.accept()
    client_name = client_socket.recv(1024)
    name=client_name.decode('ascii')
    if name=='quit':
        client_socket.close()
        break
    print(f"Accepted Connection No.{counter} with {name}")
    client_handler= threading.Thread(target=handle_client, args=(client_socket,name))
    client_handler.start()