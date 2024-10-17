import socket
# import alphabotlib as ab  # Importa la libreria Alphabot per il controllo
import threading

# Definizione della dimensione del buffer
BUFFER_SIZE = 4096

def main():
    # Inizializza l'Alphabot
    #alphabot = ab.AlphaBot()

    # Definizione dell'indirizzo del server e porta
    server_address = ("192.168.69.19", 12345)

    # Creazione del socket TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(server_address)

    # Ascolto delle connessioni
    server_socket.listen(1)
    print("Server TCP in ascolto...")
    # Thread per gestire la ricezione dei comandi
    server_thread = threading.Thread(target=ricevi_comandi, args=(server_socket,))
    server_thread.start()

def gestisci_comando(messaggio):
    # Comando nel formato: "direzione,potenza"
    comando, potenza = messaggio.split(',')
    potenza = int(potenza)
    messaggio = ""
    # Mappa dei comandi e corrispondenti movimenti
    if comando == '1':
        messaggio = "forward"
        # alphabot.forward(potenza)
    elif comando == '2':
        messaggio = "backward"
        # alphabot.backward(potenza)
    elif comando == '3':
        messaggio = "right"
        # alphabot.right(potenza)
    elif comando == '4':
        messaggio = "left"
        # alphabot.left(potenza)
    elif comando == 'stop':
        messaggio = "stop"
        # alphabot.stop()
    return messaggio
# Funzione per gestire la comunicazione con il client
def ricevi_comandi(server_socket):
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connessione accettata da {client_address}")

        while True:
            print("client connesso!")
            messaggio = client_socket.recv(BUFFER_SIZE).decode('utf-8')

            print(f"Messaggio ricevuto dal client: {messaggio}")
            mex = gestisci_comando(messaggio)

            if mex == "stop":
                break

            # Risposta al client (use client_socket here instead of server_socket)
            client_socket.send(f"Server ha ricevuto: {mex}".encode('utf-8'))

        client_socket.close()

if __name__ == "__main__":
    main()
