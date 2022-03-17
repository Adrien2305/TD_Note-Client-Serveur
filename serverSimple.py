import socket
import threading
import os
import numpy as np
from PIL import Image

class Server:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.accept_connections()
    
    def accept_connections(self):
        ip = '10.27.0.42'
        print (ip)
        port = int(input('Enter desired port --> '))

        self.s.bind((ip,port))
        self.s.listen(100)

        print('Running on IP: '+ip)
        print('Running on port: '+str(port))

        while 1:
            c, addr = self.s.accept()
            print(c)
            
            threading.Thread(target=self.handle_client,args=(c,addr,)).start()



    def handle_client(self,c,addr):
        data = c.recv(1024).decode()
        print(data)



        img_data = Image.open(data)
        img_arr = np.array(img_data)



        h,w,_= img_arr.shape # Get the width and heigth of the image

        print(h)
        print(w)



        z =  len(img_arr)
        bin_rep=bin(z)

        print(bin_rep)

        for i in img_arr.shape[1::-1]: # img.shape -> (width,height,channel)

            if(i%2 == 0):
                    
                print("pair")

            else:

                print("impair")

    
        if not os.path.exists(data):
            c.send("file-doesn't-exist".encode())

        else:
            c.send("file-exists".encode())
            print('Sending',data)
            if data != '':
                file = open(data,'rb')
                data = file.read(1024)
                while data:
                    c.send(data)
                    data = file.read(1024)

                c.shutdown(socket.SHUT_RDWR)
                c.close()
                

server = Server()
