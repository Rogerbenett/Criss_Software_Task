import socket

serverIP = '172.17.29.11'
serverPORT = 6000

serverAddress = (serverIP, serverPORT)
bufferSize = 1024

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

message = 'Hello there, my name is Salil Godbole, 2021A7PS2004P'

bytestosend = str.encode(message)

UDPClientSocket.sendto(bytestosend, serverAddress)