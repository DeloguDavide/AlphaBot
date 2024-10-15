import socket
import alphabotlib as ab  # Importa la libreria Alphabot per il controllo
import threading

# Inizializza l'Alphabot
alphabot = ab.AlphaBot()

# Definizione dell'indirizzo del server e porta
server_address = ("192.168.1.21", 12345)

# Definizione della dimensione del buffer
BUFFER_SIZE = 4096

# Creazione del socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)

# Ascolto delle connessioni
server_socket.listen(1)
print("Server TCP in ascolto...")

def gestisci_comando(messaggio):
    # Comando nel formato: "direzione,potenza"
    comando, potenza = messaggio.split(',')
    potenza = int(potenza)

    # Mappa dei comandi e corrispondenti movimenti
    if comando == '1':
        alphabot.forward(potenza)
    elif comando == '2':
        alphabot.backward(potenza)
    elif comando == '3':
        alphabot.right(potenza)
    elif comando == '4':
        alphabot.left(potenza)
    elif comando == 'stop':
        alphabot.stop()

# Funzione per gestire la comunicazione con il client
def ricevi_comandi():
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connessione accettata da {client_address}")

        while True:
            messaggio = client_socket.recv(BUFFER_SIZE).decode('utf-8')
            if not messaggio:
                break  # Se il messaggio è vuoto, esce dal ciclo

            print(f"Messaggio ricevuto dal client: {messaggio}")
            gestisci_comando(messaggio)

            # Risposta al client
            client_socket.send(f"Server ha ricevuto: {messaggio}".encode('utf-8'))

        client_socket.close()

# Thread per gestire la ricezione dei comandi
server_thread = threading.Thread(target=ricevi_comandi)
server_thread.start()
