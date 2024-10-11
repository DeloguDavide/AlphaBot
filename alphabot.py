# Importazione della libreria socket
import socket as s

# Creazione del socket TCP
alphabot_tcp = s.socket(s.AF_INET, s.SOCK_STREAM)

# Definizione dell'indirizzo del server
server_tcp_address = ("10.210.0.164", 12345)

# Associazione del socket all'indirizzo del server
alphabot_tcp.bind(server_tcp_address)

# Attivazione della modalità di ascolto del socket
alphabot_tcp.listen(1)

try:
    # Ciclo infinito per accettare le connessioni dei client
    while True:
        # Accettazione della connessione del client
        client, address = alphabot_tcp.accept()
        
        # Ricezione del messaggio dal client
        messaggio = client.recv(4096).decode('utf-8')
        
        # Ciclo per elaborare i comandi ricevuti dal client
        while messaggio != "end":
            # Suddivisione del messaggio in due parti separate da una virgola
            messaggio = messaggio.split(sep=",")
            
            # Estrazione della funzione e della potenza dal messaggio
            func = int(messaggio[0])
            power = int(messaggio[1])
            
            # Elaborazione del comando ricevuto
            if func == 1:
                messaggio = f"forward, con potenza {power}"
            elif func == 2:
                messaggio = f"backward, con potenza {power}"
            elif func == 3:
                messaggio = f"right, con potenza {power}"
            elif func == 4:
                messaggio = f"left, con potenza {power}"
            else:
                messaggio = "error"
            
            # Invio della risposta al client
            client.send(messaggio.encode('utf-8'))
            
            # Ricezione del nuovo messaggio dal client
            messaggio = client.recv(4096).decode('utf-8')
except KeyboardInterrupt:
    # Stampa di un messaggio di chiusura del socket in caso di interruzione
    print("Chiusura del socket...")

# Chiusura del socket
alphabot_tcp.close()