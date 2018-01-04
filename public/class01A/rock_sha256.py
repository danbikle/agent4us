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

def rock_sha256(msg):
    return 123,True

secret_msg = "paper";

print('Although secret_msg never changes, the commitment should change so the Adversary cannot infer the secret_msg:')

print(rock_sha256(secret_msg))
print(rock_sha256(secret_msg))
print(rock_sha256(secret_msg))
print(rock_sha256(secret_msg))

'bye'
