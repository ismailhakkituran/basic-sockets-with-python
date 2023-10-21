from socket import * 
    
serverPort = 12000 
serverSocket = socket (AF_INET, SOCK_DGRAM)
serverSocket.bind (('', serverPort)) 
print("Sunucu almak icin hazir") 

while True: 
    message, clientAddress = serverSocket.recvfrom(2048) 
    modifiedMessage = message.decode().upper() 
    serverSocket.sendto(modifiedMessage.encode(),clientAddress)
    print (modifiedMessage)
