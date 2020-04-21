import socket


UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 1024



def send():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("Connected to the server.")
        print("Starting a file (upload.txt) upload...")
        with open("upload.txt","r") as f:
            for message in f.readlines():
                input_data =""
                s.sendto(message.encode(),(UDP_IP, UDP_PORT))
                data,ip= s.recvfrom(BUFFER_SIZE)
                input_data =data.decode()
                while not input_data:
                    s.sendto(message.encode(),(UDP_IP, UDP_PORT))
                    data,ip= s.recvfrom(BUFFER_SIZE)
                    input_data =data.decode()   
                print("received ack: {}: from the server".format(input_data))
                
    except socket.error:
        print("Error! {}".format(socket.error))
        exit()
    s.sendto("quit".encode(), (UDP_IP, UDP_PORT))
    print("File upload successfully completed.")


send()