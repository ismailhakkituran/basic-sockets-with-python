import time
from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket (AF_INET, SOCK_DGRAM)



while True:
    message = 'dddddddddd'
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom (2048)
    print (modifiedMessage.decode())
    time.sleep(1)
