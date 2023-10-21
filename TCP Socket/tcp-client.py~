from socket import *

serverName = 'localhost'
serverPort = 12000 

clientSocket = socket (AF_INET, SOCK_STREAM) 
clientSocket.connect((serverName, serverPort)) 

sentence = input('Kucuk harfli cumleler giriniz:') 
print('Girilen mesaj: ', sentence) 
print('Encoded mesaj: ', sentence.encode() )

clientSocket.send(sentence.encode()) 

modifiedSentence = clientSocket.recv(1024) 
print('Sunucudan gelen mesaj: ', modifiedSentence.decode()) 
clientSocket.close()
