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
    # I should start sha creation by specifying a range of integers.
    # If the range is large, the commitment should be hidden:
    range_i  = int(1e+9)
    # I should pick a random number from the range:
    random_i = secrets.choice(range(range_i))
    # I should convert the number to a string and concatenate it with msg
    random_s     = str(random_i)
    random_msg_s = random_s + msg_s
    # I should generate the hash:
    my_hashlib = hashlib.sha256()
    my_hashlib.update(random_msg_s.encode('utf-8'))
    # I should convert it to a readable string:
    secure_hash_s = my_hashlib.hexdigest().upper()
    # random_i and secure_hash_s should be able to verify msg_s:
    return msg_s, random_i, secure_hash_s

print('Although secret_msg never changes, the commitment should change so the Adversary cannot infer the secret_msg:')

secret_msg = "paper";
print(rock_sha256(secret_msg))
print(rock_sha256(secret_msg))

secret_msg = "scissors";
print(rock_sha256(secret_msg))
print(rock_sha256(secret_msg))

'bye'
