
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
- Before establishing communication between the server and client, we need to execute
the server script first.
- We need to download images img.png / img1.png/ img2.png... in server
- When we have established the communucation between the two entity , the script will display:
- 1 - if the total pixel of the images downloaded is even - `it will display 'pair'`
- 2 - if the total pixel of the images downloaded is odd - `it will display 'impair'`
