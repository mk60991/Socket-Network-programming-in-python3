C:\Users\hp\AppData\Local\Programs\Python\Python36
import socket
mysocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysocket.connect(("192.168.239.1",4444))
data=mysocket.recv(1024)
print(data)
mysocket.send(b'hello client')
mysocket.close()
