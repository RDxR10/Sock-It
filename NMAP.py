import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
target = input('[+] Enter target IP: ')
def scanner(port):
	try:
		sock.connect((target,port))
		return True
	except:
		return False
for portNumber in range(20,200):
	print("Scanning port", portNumber)
	if scanner(portNumber):
		print('[*] Port', portNumber, '/tcp', 'is open')
