import socket as sck
import config
g = config.g
N = config.N

ip='localhost'
port=6300

c = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
tupla = (ip,port)
c.connect((ip,port))

while(1):
    a = int(input("inserire a: "))
    if(a<N):
        break
    print("numero non valido ")

A = (g**a) % N

print(A)

c.sendto(str(A).encode(),tupla)

B = int(c.recv(4096).decode())
print(f"ricevuto : {B}")
K = (B**a) % N

print(f"il numero finale è {K}")



