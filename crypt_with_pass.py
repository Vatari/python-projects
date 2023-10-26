from cryptography.fernet import Fernet


key = Fernet.generate_key()

f = Fernet(key)

encrypt_token = f.encrypt(b'Hello Cryptography')
#encrypt_token = f.encrypt(f"b"{input()}")"

decypt_token = f.decrypt(encrypt_token)

print(decypt_token)