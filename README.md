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
- UDP

## How to establish the communication 

| Name | Testing|
| ------ | ------ |
| Server | ``` python3 serverSimple.py ``` |
| Client | ``` python3 clientSimple.py img.jpeg``` |

## Server/Client Explanation
- When establishing the communication between the server and client, we need to execute
the server script first then afterward the client side.
- The clientSimple.py should be placed on the client side and it should have the same ip address as the server side.
- The serverSimple.py should be placed on the server side and it should have the same ip address as the client side.
- When we have established the communucation between the two entities , the script will import and display:
- 1 - if the total pixel of the image downloaded is even - `it will display 'pair'`
- 2 - if the total pixel of the image downloaded is odd - `it will display 'impair'`
