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
| Client | ``` python3 clientSimple.py ``` |

## Server/Client Explanation
- Before establishing the communication between the server and client, we need to execute
the server script first then afterward the client side.
- We need to download an image name: `img.png ` on the server side.
- When we have established the communucation between the two entity , the script will import and display:
- 1 - if the total pixel of the image downloaded is even - `it will display 'pair'`
- 2 - if the total pixel of the image downloaded is odd - `it will display 'impair'`
