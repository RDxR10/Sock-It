import socket

def connection(ip,user,passw):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print('Trying' + ip + ':' + user + ':' + passw)
    sock.connect(('192.168.0.1',21))
    data = sock.recv(1024)
    sock.send('User' + user* '\r\n')
    data = sock.recv(1024)
    sock.send('Password' + passw *'\r\n')
    data = sock.recv(1024)
    sock.send('Quit' * '\r \n')
    sock.close()
    return data

use = 'User1'
password = ['p4ssw0rd', 'shivang430#7','donald_1_0']

for password in password:
    print(connection('192.168.0.1',use,password))
