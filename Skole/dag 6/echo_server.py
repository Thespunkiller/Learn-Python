import socket

host = "127.0.0.1"
port = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host,port))
    s.listen()
    conn,addr = s.accept()
    with conn:
         print("connected",addr)
         while True:
             data = conn.recv(1024)
             if not data:
                 break
             #conn.sendall((data).upper())

             if data== b"one":
            
                data = b"hej"
                conn.sendall(data)

             elif data== b"two":
                 data = b"fuck dig"
                 conn.sendall(data)
            
             else:
                break
                

             
    print("fuck af")
                
         