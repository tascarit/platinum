import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("platinum.myddns.me", 9998))

sock.send("sus".encode())
sock.close()