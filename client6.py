import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1",4444))
data=s.recv((2048).decode('UTF-8'))
print(data)
s.send(("hello i ma client").encode('UTF-8'))
s.close()
