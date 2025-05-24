import socket
import threading
from crypto_utils import encrypt_message, decrypt_message, KEY

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                decrypted = decrypt_message(message, KEY)
                print(f"\r\n🔓 Decrypted: {decrypted}\n> ", end="")
        except:
            print("\n⚠️ Connection closed.")
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 9999))

    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    print("🔐 Connected. Type messages to send:")
    while True:
        msg = input("> ")
        if msg:
            encrypted = encrypt_message(msg, KEY)
            client.send(encrypted.encode())

if __name__ == "__main__":
    main()
