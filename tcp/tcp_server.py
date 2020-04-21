import socket
from threading import Thread

TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024

def listen_forever():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(5)
    print("Server started at port 5000.")
   
    while True:
        conn, addr = s.accept()
        try:
            Thread(target=handle_request, args=(conn,addr,BUFFER_SIZE)).start()
        except:
            print("Thread did not start.")

def handle_request(connection,address,buffer_size):
    data =connection.recv(buffer_size)
    input_data = data.decode().split(",")
    print("Connected Client: ",input_data[0], "at ",address)
    while True:
        if "quit" in input_data:
            connection.close()
            print(f'Connection closed at address:{address}')
            break
        else:
            print(f"Received data {input_data[0]}: {input_data[1]}")
            connection.send("pong".encode())
        data =connection.recv(buffer_size)
        input_data = data.decode().split(",")
listen_forever()