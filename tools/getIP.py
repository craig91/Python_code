import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

print("Your computer host name is " + hostname)
print("Your computer IP Address is: " + IPAddr)
