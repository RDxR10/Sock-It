import socket
HOST="10.5.8.10"
PORT=77

#sock_obj
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    s.listen()
    s.sendall('Hello, Friend')
    conn, addr = s.accept()
    #s.bind((target_host,target_port))
    data=s.recv(1024)
print('Received',repr(data))
#with conn:
    #print("Connected by",addr)
    #while True:
        #data = conn.recv(1024)
        #if not data:
            #break
        #conn.sendall(data)
