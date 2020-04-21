import socket
import sys
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024
MESSAGE = "ping"

def send():
    argumentList = sys.argv 
    id = argumentList[1]
    delay = int(argumentList[2])
    n = int(argumentList[3])
    i = 1
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    while i<=n:
        print("Sending data: ",MESSAGE)
        s.send(f"{id},{MESSAGE}".encode())
        data = s.recv(BUFFER_SIZE)
        print("Received data: ", data.decode())
        i+=1
        time.sleep(delay)
    s.send("quit".encode())
    s.close()
    

send()