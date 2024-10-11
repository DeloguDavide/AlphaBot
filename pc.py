import socket as s

albhabot_address = ("192.168.25.19", 2345)

client_TCP = s.socket(s.AF_INET, s.SOCK_STREAM)
client_TCP.connect(albhabot_address)

while True:
    print("client Connesso")
    message = input()
    client_TCP.send(message.encode())
    data = client_TCP.recv(1024).decode()
    if data == "0":
        break