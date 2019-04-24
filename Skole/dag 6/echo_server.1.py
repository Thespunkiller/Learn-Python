#opgave 3
import socket
from auth import create,login

host = "127.0.0.1"
port = 8080



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host,port))
    s.listen()
    conn,addr = s.accept()
    with conn:
        print("connected",addr)

        close = False
        while not close:
            data = conn.recv(1024)
             #conn.sendall((data).upper())

            if data== b"one":
            
                data = b"hej"
                conn.sendall(data)

            elif data== b"two":
                data = b"fuck dig"
                conn.sendall(data)
            
            elif data == b"create":
                conn.sendall(b"please enter username")
                username = conn.recv(1024).decode("utf-8")
                conn.sendall(b"please enter password")
                password = conn.recv(1024).decode("utf-8") 
                conn.sendall(b"user has been created")  
                # create(username, password)  

            else:
                close = True
                conn.sendall(b"server is closing")
                

             
    print("fuck af")
                
         