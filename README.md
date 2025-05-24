# Encrypted Messaging System

A secure, encrypted messaging system using Python sockets and AES (CBC mode) encryption.

## 🔐 Features
- Encrypted real-time messaging using AES (CBC)
- Secure TCP-based communication
- Built with `PyCryptodome` for robust crypto primitives
- Threaded server handling multiple clients

## ⚙️ Setup
1. `pip install -r requirements.txt`
2. Run `server.py` first
3. Then run multiple instances of `client.py` to test

## 🧠 Security Note
- This project uses a shared symmetric key (`KEY`) generated once on runtime. For a real-world app, implement proper key exchange (e.g., Diffie-Hellman, RSA).

## 📸 Output Screenshots

### Server Running
![Server Screenshot](images/server screenshot.png)

### Client 1 & 2
![Client 1 Screenshot](images/clients screenshots.png)


*Make sure to place these images inside a `/images` folder.*
