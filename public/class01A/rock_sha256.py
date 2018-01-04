"""
rock_sha256.py

This script creates and demonstrates a function which converts a msg
into a random number, r, and SHA-256(r|msg).

Ref:
http://cryp4.us/cclasses/class01A#rock

Demo:
python rock_sha256.py
"""

import hashlib
import secrets

def rock_sha256(msg_s):
    # Fails: random_i = secrets.choice(range(2**256))
    # So,
    # I should create a list with 64 random values, each tween 0 and 16:
    hex_l = [hex(secrets.choice(range(16))) for place_i in range(64)]
    # I see this list as a random number between 0 and 16**64 (is 2**256)
    # I should convert the list to a string:
    random_s     = ''.join(hex_l).replace('0x','').upper()
    # I should move towards hiding msg_s:
    random_msg_s = random_s + msg_s
    # I should access SHA-256 API:
    my_hashlib = hashlib.sha256()
    # I should hide msg_s:
    my_hashlib.update(random_msg_s.encode('utf-8'))
    # I should convert it to a readable string:
    secure_hash_s = my_hashlib.hexdigest().upper()
    # random_s and secure_hash_s should be able to verify msg_s:
    return random_s, msg_s, secure_hash_s

print('Although secret_msg never changes, the commitment should change so the Adversary cannot infer the secret_msg:')

secret_msg = "paper"
print(rock_sha256(secret_msg))
print(rock_sha256(secret_msg))

secret_msg = "scissors"
print(rock_sha256(secret_msg))
print(rock_sha256(secret_msg))

'bye'
