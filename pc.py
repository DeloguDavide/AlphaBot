# Importazione della libreria socket
import socket as s

# Definizione dell'indirizzo del server
server_tcp_address = ("10.210.0.49", 12345)

# Creazione del socket TCP del client
client_tcp = s.socket(s.AF_INET, s.SOCK_STREAM)

try:
    # Connessione al server
    client_tcp.connect(server_tcp_address)
    
    # Stampa delle istruzioni per l'utente
    print("""in questo programma gestirai la posizione virtuale di un robot,
    per gestirla devi utilizzare le funzioni:
    1 - forward
    2 - backward
    3 - right
    4 - left
    per uscire dalla connessione scrivi 'end'""")
    
    # Input dell'utente per la funzione e la potenza
    messaggio=input("Inserisci il numero della funzione e la potenza tra 0-100(num, power):  ")   
    
    # Ciclo per inviare i comandi al server
    while messaggio!="end":
        # Invio del messaggio al server
        client_tcp.send(messaggio.encode('utf-8'))
        
        # Ricezione della risposta dal server
        messaggio = client_tcp.recv(4096).decode('utf-8')
        
        # Stampa della risposta del server
        print(f"Il server dice: {messaggio}")
        
        # Input dell'utente per la funzione e la potenza
        messaggio=input("Inserisci il numero della funzione e la potenza tra 0-100(num, power):  ")

except KeyboardInterrupt:
    # Stampa di un messaggio di interruzione del programma
    print("\nProgramma interrotto da CTRL + C")

# Stampa di un messaggio di chiusura della connessione
print("Chiusura della connessione...")

# Chiusura del socket del client
client_tcp.close()