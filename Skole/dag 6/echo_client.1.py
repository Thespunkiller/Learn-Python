#opgave 3
import socket
import datetime
host = "127.0.0.1"
port = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host,port))

    #dato print
    #date = datetime.datetime.now()
    #date_string = date.strftime("%D/%T")
    #s.sendall(date_string.encode("utf-8"))
    close = False
    while not close:
        inp = input()
        s.sendall(inp.encode("utf-8"))
        data = s.recv(1024)
        print("Thanks i recived ur message:", repr(data))
        if inp == "close":
            close = True
#print("Thanks i recived ur message:", repr(data)[2:-1])
# print("Thanks i recived ur message:", repr(data))