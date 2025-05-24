from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

KEY = b'ThisIsASecretKey' # Must be 16 bytes long for AES-128

def encrypt_message(message, key=KEY):
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ct_bytes = cipher.encrypt(pad(message.encode(), AES.block_size))
    return base64.b64encode(iv + ct_bytes).decode()

def decrypt_message(cipher_text, key=KEY):
    data = base64.b64decode(cipher_text)
    iv = data[:16]
    ct = data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode()
