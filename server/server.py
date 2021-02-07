import socket

s = socket.socket()
s.bind(('', 5001))

s.listen(1)

while True:
    conn, addr = s.accept()
    print addr, 'connected.'

    action = conn.recv(1).rstrip()
    if(action == 'r'):
        filename = conn.recv(1024).rstrip()
        file = open(filename)

        for line in file.readlines():
            conn.sendall(line)
    else:
        filename = conn.recv(1024).rstrip()
        file = open(filename, 'w')

        while(True):
            data = conn.recv(1024)
            if(len(data) == 0):
                break
            file.write(data)

    file.close()
    conn.close()
    print addr, 'disconnected.'
