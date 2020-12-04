import socket as sck
import config
g = config.g
N = config.N

ip = 'localhost'
port = 6300
tupla=(ip,port)
s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)

s.bind(tupla)

s.listen()

conn,mittente = s.accept()

while(1):
    b = int(input("inserire b: "))
    if(b<N):
        break
    print("numero non valido ")

print(f"b = {b}")

A = int(conn.recv(4096).decode())
print(f"A ricevuto = {A}")
B  = (g**b) % N
print(f"B inviato = {B}")
conn.sendall(str(B).encode())

K = (A ** b)%N

print(f"il numero finale è {K}")
