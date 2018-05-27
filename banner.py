import socket
socket.setdefaulttimeout(2)
s=socket.socket()
ip=input("enter target ipo\:")
port=int(input("enter target port"))
s.connect((ip,port))
print(s.recv(1024).decode('UTF-8'))
s.close()
