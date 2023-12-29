import socket
import sys

# HOST = '127.0.0.1'
# PORT = 7777

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET is ipv4, SOCK_STREAM is a port

# s.connect((HOST, PORT))



hostName = "google.com"

ipAddress = socket.gethostbyname(hostName)

print("IP of the host name {} is: {}".format(hostName, ipAddress))