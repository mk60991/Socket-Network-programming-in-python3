import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("127.0.0.1",4444))
s.listen(5)
(client,(ip,port))=s.accept()
client.send(("hello i ma server").encode('UTF-8'))
data=client.recv((2048).decode('UTF-8'))
print(data)
s.close()
