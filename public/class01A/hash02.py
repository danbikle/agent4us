"""
hash02.py

This script should demo-how-to operate a popular Python implementation
of a Cryptographic Hash Function.

python hash02.py
"""

from cryptography.fernet import Fernet

# I should generate a privatekey:
privatekey = Fernet.generate_key()

# I should create a fernet object from the key and cryptography-API:
fernet = Fernet(privatekey)

# I should declare a msg I want to encrypyt:
calif_bs = b"Today is Dec 27, 2017 and the weather in California is perfect."

# I should encrypt the message:
cryptographic_hash = fernet.encrypt(calif_bs)

# I should look at the cryptographic_hash:
print('cryptographic_hash:')
print(cryptographic_hash)

# I should decrypt cryptographic_hash:
print('fernet.decrypt(cryptographic_hash):')
print(fernet.decrypt(cryptographic_hash))

'bye'
