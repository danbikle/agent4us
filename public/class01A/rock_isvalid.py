"""
rock_isvalid.py

This script validates that SHA-256(r|msg) matches a given secure-hash is True or False.

Ref:
http://cryp4.us/cclasses/class01A#rock

Demo:
python rock_isvalid.py
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

# I should try some values which are valid and invalid.
# I got the valid values from rock_sha256.py

print(rock_isvalid(652897841, 'paper', '0DBEEB821799443AE3E674D27B74FCBD35498E0F87EC80DAC918349063069701'))
print(rock_isvalid(906623637, 'paper', 'BE6B13C90F049E94F780F11506F44E3D6B9CE71D216B2E1528883A6AB19EA28D'))
print(rock_isvalid(491186498, 'scissors', '112F769D380125C2E97DDCC46793776EC6C388D68E5C506A61D581246AB4201D'))
print(rock_isvalid(21968910, 'scissors', '5DD1C3D939FA09B68146F0C1D34EDED9F8537D0ABF0EC77E06191CA592833AE3'))
print(rock_isvalid(121968910, 'scissors', '5DD1C3D939FA09B68146F0C1D34EDED9F8537D0ABF0EC77E06191CA592833AE3'))

'bye'
