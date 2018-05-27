import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("127.0.0.1",1337))
clientdata,addr=s.recvfrom(2000)
print(clientdata)
print("address of client",addr)
s.sendto("hello i am server".encode('UTF-8'),addr)
s.close()
