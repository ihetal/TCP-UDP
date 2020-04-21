import socket
import random

UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 1024
MESSAGE = "pong"

def listen_forever():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", UDP_PORT))
    print("Server started at port 4000.")
    data, ip = s.recvfrom(BUFFER_SIZE)
    print("Accepting a file upload...")
    file =open('output.txt','w+')
    while True:
        # get the data sent to us
        
        message = data.decode(encoding="utf-8").strip()
        if message:
            if message =="quit":
                file.close()
                print("Upload successfully completed.")
                exit()
            # reply back to the client
            file.write(data.decode(encoding="utf-8").strip())
            file.write("\n")
            my_ack =str(random.randrange(10000, 10000000,2))
            s.sendto(my_ack.encode(), ip)
        else:
            continue
        data, ip = s.recvfrom(BUFFER_SIZE)


listen_forever()