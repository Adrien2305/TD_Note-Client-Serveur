# TD_Note-Client-Serveur
# Communication inter-processus
## --------------------------------------------------------------------------------------
## Installation of libraries python3
```sh
sudo apt install python3-numpy
sudo apt install python3-pip
sudo pip3 install pillow
```
## Communication protocole used 
- UDP
## clientSimple.py
```sh
import socket

msgFromClient       = "Hello Server"

bytesToSend         = str.encode(msgFromClient)

serverAddressPort   = ("10.27.0.42", 12345)

bufferSize          = 1024


# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Send to server using created UDP socket

UDPClientSocket.sendto(bytesToSend, serverAddressPort)


msgFromServer = UDPClientSocket.recvfrom(bufferSize)


msg = "Message from Server {}".format(msgFromServer[0])

print(msg)
```
## serverSimple.py
```sh
import socket
import numpy as np
from PIL import Image

img_data = Image.open('img.jpeg')
img_arr = np.array(img_data)

z =  len(img_arr)

for i in img_arr.shape[1::-1]: # img.shape -> (width,height,channel)

    if(i%2 == 0):

    	msgFromServer= "pair"

    else:

        msgFromServer= "impair"

localIP     = "10.27.0.42"

localPort   = 12345

bufferSize  = 1024

bytesToSend         = str.encode(msgFromServer)

# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

# Listen for incoming datagrams

while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    
    print(clientMsg)
    print(clientIP)

    # Sending a reply to client

    UDPServerSocket.sendto(bytesToSend, address)
```
## How to establish the communication 

| Name | Testing|
| ------ | ------ |
| Server | ``` python3 serverSimple.py ``` |
| Client | ``` python3 clientSimple.py ``` |
| Import image | ``` python3 img.py ``` |


## Download an image in server
- img.jpeg
## 
## Import image script
```sh
import numpy as np
from PIL import Image



#img_arr = img_arr - 180
#new_img = Image.fromarray(img_arr)
#new_img.save("altered_img.png")

def fletcher32(length):
    w_len = length
    c0 = 0
    c1 = 0
    x = 0

    while w_len >= 360:
        for i in range (360):
            c0 = c0 
            c1 = c1 + c0
            x = x + 1
        c0 = c0 % 65535
        c1 = c1 % 65535
        w_len = w_len - 360
    
    for i in range (w_len):
       c0 = c0 
       c1 = c1 + c0
       x = x + 1
    c0 = c0 % 65535
    c1 = c1 % 65535
    return (c1 << 16 | c0)

img_data = Image.open('img.jpeg')
img_arr = np.array(img_data)



h,w,_= img_arr.shape # Get the width and heigth of the image

print(h)
print(w)



z =  len(img_arr)
fletcher32(z)

for i in img_arr.shape[1::-1]: # img.shape -> (width,height,channel)

    if(i%2 == 0):
            
        print("pair")

    else:

        print("impair")
```
