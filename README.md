## TD_Client/Server By Adrien Esther
This project work is to create a client Server application and set up a communication protocol (UDP) between the two entities. On the server we will have the images example ```img.jpeg``` then the client will ask the server to retrieve the image.
## --------------------------------------------------------------------------------------
## Installation of python3 libraries
```sh
sudo apt install python3-numpy
sudo apt install python3-pip
sudo pip3 install pillow
```
## Communication protocole used 
- TCP
Transmission Control Protocol (TCP) is a standard that defines how to establish and maintain a network conversation by which applications can exchange data. 
TCP works with the Internet Protocol (IP), which defines how computers send packets of data to each other.
## How to establish the communication 

| Entity | Testing|
| ------ | ------ |
| Server | ``` python3 serverSimple.py ``` |
| Client | ``` python3 clientSimple.py``` |

## Server/Client Explanation
- The clientSimple.py should be placed on the client side and it should have the same ip address as the server side.
- The serverSimple.py should be placed on the server side and it should have the same ip address as the client side.
- When establishing the communication between the server and client, we need to execute
the server script first then afterward the client side.

## How to Run the Application
- Run the serverSimple.py in server
- Enter a port e.g: 8081
- Run the clientSimple.py in client
- Enter the ip address : 10.27.0.42
- Re enter the port we have inserted in server : 8081
- Then we enter the file name that the client want to retrieve for example : ```img.jpeg```

```Server```
```sh
10.27.0.42
Enter desired port --> 8081 
Running on IP: 10.27.0.42
Running on port: 8081
```
```Client```
```sh
Enter ip --> 10.27.0.42
Enter port --> 8081
Enter file name on server --> img.jpeg
img.jpeg successfully downloaded.
0b10110111
impair
impair
```
