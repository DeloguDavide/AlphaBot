import socket
from pynput import keyboard

# Definizione dell'indirizzo del server
server_tcp_address = ("192.168.1.21", 12345)

# Creazione del socket TCP del client
client_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_tcp.connect(server_tcp_address)

# Funzione per inviare il comando al server
def invia_comando(func, power=50):
    messaggio = f"{func},{power}"
    client_tcp.send(messaggio.encode('utf-8'))

# Funzione per gestire i tasti premuti
def on_press(key):
    try:
        if key.char == 'w':
            invia_comando('1')  # Avanti
        elif key.char == 's':
            invia_comando('2')  # Indietro
        elif key.char == 'd':
            invia_comando('3')  # Destra
        elif key.char == 'a':
            invia_comando('4')  # Sinistra
        elif key.char == 'q':
            invia_comando('stop')  # Stop
    except AttributeError:
        pass

# Listener per i tasti premuti
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

# Chiudi la connessione TCP
client_tcp.close()
