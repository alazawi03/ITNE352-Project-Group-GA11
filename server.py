import socket
import time
import threading
import urllib.error
from urllib.request import urlopen

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(("127.0.0.1", 49999))
ss.listen(3)
sock_a, sockname = ss.accept()

sock_a.send("Enter airport code (arr_icao)".encode())