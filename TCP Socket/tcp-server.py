from socket import * 

serverPort = 12001 
serverSocket = socket(AF_INET, SOCK_STREAM) 
serverSocket.bind(('', serverPort)) 
serverSocket.listen(1) 
print("Sunucu almak icin hazır") 


while True: 
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    print('Sunucuya gelen mesaj: ', sentence )
    capitalizedSentence = sentence.upper()
    print('İşlem sonucu mesaj: ', capitalizedSentence )
    connectionSocket.send(capitalizedSentence.encode()) 
connectionSocket.close()
