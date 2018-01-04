"""
rock_isvalid.py

This script validates that SHA-256(r|msg) matches a given secure-hash is True or False.

Ref:
http://cryp4.us/cclasses/class01A#rock

Demo:
python rock_isvalid
"""

import hashlib

def rock_isvalid(r_i, msg_s, secure_hash_s):
    random_msg_s = str(r_i)+msg_s
    # I should generate the hash:
    my_hashlib = hashlib.sha256()
    my_hashlib.update(random_msg_s.encode('utf-8'))
    # I should convert it to a readable string:
    my_secure_hash_s = my_hashlib.hexdigest().upper()
    return my_secure_hash_s == secure_hash_s

msg_s = "paper";
print(rock_sha256(msg_s))
print(rock_sha256(msg_s))

msg_s = "scissors";
print(rock_sha256(msg_s))
print(rock_sha256(msg_s))

'bye'
