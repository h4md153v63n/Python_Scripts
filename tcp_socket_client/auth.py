import socket
import hashlib
from urllib3.connectionpool import xrange

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to an IP with Port, could be a URL
sock.connect(('137.135.141.116', 6666))

# Send some data, this method can be called multiple times
sock.send("hamdi".encode())

# Receive up to 4096 bytes from a peer
n = int(sock.recv(4096).decode())
print("NONCE VALUE\t\t : " + str(n))


def encrypt_password(hashed_password):
    sha256pass = hashlib.sha256(hashed_password.encode()).hexdigest()
    return sha256pass


hash_password = encrypt_password("12345")

if n > 2:
    for i in xrange(n - 1):
        hash_password = encrypt_password(hash_password)
        if i + 2 == n - 1:
            sock.send(hash_password.encode("utf-8"))
            print("SHA256 HASH VALUE\t : " + hash_password)
elif n == 2:
    sock.send(hash_password.encode("utf-8"))
    print("SHA256 HASH VALUE\t : " + hash_password)

print("STATUS\t\t\t : " + sock.recv(4096).decode())
