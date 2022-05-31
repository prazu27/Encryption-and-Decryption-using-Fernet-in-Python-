from cryptography.fernet import Fernet
key = Fernet.generate_key()

with open('secret.key','wb') as new_key_file:
   new_key_file.write(key)

print(key)

msg = "Into the valley of death, rode this 600"

msg = msg.encode()

f = Fernet(key)

ciphertext = f.encrypt(msg)

print(ciphertext)

with open('secret.key','rb') as my_private_key:
   key = my_private_key.read()

f = Fernet(key)

cleartext = f.decrypt(ciphertext)

cleartext = cleartext.decode()

print(cleartext)



