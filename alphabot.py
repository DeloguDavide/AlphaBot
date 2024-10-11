import socket as s

alphabot_address = ("192.168.25.19", 2345)

alphabot_TCP = s.socket(s.AF_INET, s.SOCK_STREAM)
alphabot_TCP.bind(alphabot_address)
alphabot_TCP.listen(1)

while True:
    client, address = alphabot_TCP.accept()
    while True:
        messaggio = client.recv(4096).decode('utf-8')
        if messaggio == "end":
            break
        print(messaggio)
        client.send(messaggio.encode("utf-8"))
    print("chiusura connessione...")
    client.send("0".encode("utf-8"))
    client.close()
alphabot_TCP.close()