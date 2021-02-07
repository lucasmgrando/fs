import socket
import sys

s = socket.socket()
s.connect(('', 5001))

filename = sys.argv[1]

if 'w' in sys.argv:
    s.sendall('w')

    file = open(filename)
    s.sendall(filename)

    for line in file.readlines():
        s.sendall(line)
else:
    s.sendall('r')

    s.sendall(filename)

    file = open(filename, 'w')
    while(True):
        data = s.recv(1024)
        if(len(data) == 0):
            break
        file.write(data)

file.close()
s.close()
