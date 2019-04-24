import socket

def recive(conn):
    return conn.resv(1024).decode("utf-8")

def send(conn, message):
    conn.sendall(message.encode("utf-8"))

def send_recive(conn, message):
    send(conn, message)
    return recive(conn)
