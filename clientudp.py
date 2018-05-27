import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect(("127.0.0.1",1337))
s.sendto(b'from client',("127.0.0.1",1337))
data=s.recvfrom(2048)
print(data)
s.close()
