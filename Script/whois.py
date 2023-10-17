import socket

domain = input("input domain: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("whois.internic.net", 43))
s.send(f"{domain}\r\n".encode())

while True:
    v = s.recv(1024)
    if not v:
        break
    decoded = v.decode()
    print(decoded)

s.close()
