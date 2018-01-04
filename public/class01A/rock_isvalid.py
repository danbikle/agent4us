"""
rock_isvalid.py

This script validates that SHA-256(r|msg) matches a given secure-hash is True or False.

Ref:
http://cryp4.us/cclasses/class01A#rock

Demo:
python rock_isvalid.py
"""

import hashlib

def rock_isvalid(random_s, msg_s, secure_hash_s):
    random_msg_s = random_s + msg_s
    # I should generate the hash:
    my_hashlib = hashlib.sha256()
    my_hashlib.update(random_msg_s.encode('utf-8'))
    # I should convert it to a readable string:
    my_secure_hash_s = my_hashlib.hexdigest().upper()
    return my_secure_hash_s == secure_hash_s

# I should try some values which are valid and invalid.
# I got the valid values from rock_sha256.py

print(rock_isvalid('2712BEB0DE932F75662638AD18FD5A3A218655B9C3C41DD46C372A33E466FA56', 'paper', 'D29209ACE47A443AA837E99D468861AC6655EB165E59EE5337E93326AE7F6860'))
print(rock_isvalid('16C1E444DAAB51C60769CF682DF2C8732E45EB72BFF011CD27C780614DD77FF5', 'paper', '6B0D6DCC565FB1BE9BB0138D68AAD772339EBCAA5CB6B98726A730D0C7C5645D'))
print(rock_isvalid('C8110BCB85F56C7D7DD21CE7823C9663C3390DF2025892536D223FA30D391C98', 'scissors', '2391213B7246A178A1B8BDF290E716B9AFD4DED67803327FA5AFC24A0D63EB00'))
print(rock_isvalid('3AED100B0D26F0CE0F15BA3374D71BAD523A37236653A458BA3DFD38D934A959', 'scissors', 'EA5456CD0A5B7C370B17BBC8B6CD9B6938CC28161ADB686F1E627DA47BB0F3B2'))

# s.b. invalid:
print(rock_isvalid('3AED100B0D26F0CE0F15BA3374D71BAD523A37236653A458BA3DFD38D934A958', 'scissors', 'EA5456CD0A5B7C370B17BBC8B6CD9B6938CC28161ADB686F1E627DA47BB0F3B2'))

'bye'
