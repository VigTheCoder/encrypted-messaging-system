import socket
import threading
from crypto_utils import decrypt_message, encrypt_message, KEY

clients = []

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    clients.append(conn)
    try:
        while True:
            msg = conn.recv(1024).decode()
            if msg:
                print(f"[RECEIVED] From {addr}: {msg}")
                decrypted = decrypt_message(msg, KEY)
                print(f"[DECRYPTED] {decrypted}")
                broadcast(msg, conn)
    except Exception as e:
        print(f"[DISCONNECTED] {addr}: {e}")
        if conn in clients:
            clients.remove(conn)
        conn.close()

def broadcast(message, sender_conn):
    for client in clients:
        if client != sender_conn:
            try:
                client.send(message.encode())
            except Exception as e:
                print(f"[ERROR] Could not send to a client: {e}")
                clients.remove(client)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9999))
    server.listen()
    print("[STARTED] Server is listening...")
    
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
