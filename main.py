from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

salt = b'\xb9\x14\xd3\x12G\xe0H\xef\xa8\x0f\xe0y\xf9\xcdI\x123$\xd7l\xb7g\xbe<{<~d\xa1\xef"\xdb'
password = "MyPassword"

key = PBKDF2(password, salt, 32)

message = b"Hello Secret World"
cipher = AES.new(key, AES.MODE_CBC)
ciphered_data = cipher.encrypt(pad(message, AES.block_size))

with open('encrypted.bin', 'wb') as f:
    f.write(cipher.iv)
    f.write(ciphered_data)
    
with open('encrypted.bin', 'rb') as f:
    iv = f.read(16)
    decrypt_data = f.read()
    
cipher = AES.new(key, AES.MODE_CBC, iv = iv)
original = unpad(cipher.decrypt(decrypt_data), AES.block_size)

print(original)

with open('key.bin', 'wb') as f:
    f.write(key)