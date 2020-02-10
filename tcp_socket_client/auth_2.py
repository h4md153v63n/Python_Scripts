# -*-coding:utf-8-*-
import socket
import hashlib

# SOCK_STREAM tcp için; SOCK_DGRAM udp için kullanılır.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# port ile ip adresine bağlan, url de olabilir.
sock.connect(('137.135.141.116', 6666))

# server'a data gönder, bu defalarca tekrarlanabilir.
sock.send(input("kullanıcı adı giriniz: ").encode())

# serverdan cevabı al.
n = int(sock.recv(4096).decode())
print("NONCE VALUE\t\t : " + str(n))

sock.send("".encode("utf-8"))

print("STATUS\t\t\t : " + sock.recv(4096).decode())


