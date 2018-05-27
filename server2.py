import socket
mysocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysocket.bind(("192.168.239.1",4444))
mysocket.listen(5)
(client,(ip,port))=mysocket.accept()
client.send(b'hello server')
data=client.recv(2018)
print(data)
mysocket.close()
