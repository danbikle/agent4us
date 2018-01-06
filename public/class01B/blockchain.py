"""~/cryp4/public/class01B/blockchain.py

This script should demo how to create a very simple Blockchain with Python.

The Blockchain class will be similar to the LinkedList class I
demonstrated earlier.

But each element, a simple dictionary, has an additional attribute called
secure_hash_ofnext.

Additionally, Blockchain has a Boolean class-method named isvalid().

Demo:
python blockchain.py
"""

import hashlib

# I should create my first member of the linked-list:
adam_d = {'txt': 'Genesis says Adam is here.'}
# I should create more members:
eve_d = {'txt': 'Eve says Hi.'}
sam_d = {'txt': 'Sam is short for either Samantha or Samuel.'}
# I have members but they are not linked yet.

class Blockchain():
    """Class for creating a data structure called a 'Linked-List'."""
    def __init__(self):
        self.head = {'list_head': True, 'next': None, 'secure_hash_ofnext': None, 'txt': None}
    def hashit(in_s):
        my_hashlib = hashlib.sha256()
        in_b       = in_s.encode('utf-8')
        my_hashlib.update(in_b)
        retunr my_hashlib.digest()
        
    def add_member(self, new_member_d):
        if self.head['next']:
            nextmem_d            = self.head['next']
            new_member_d['next'] = nextmem_d
            hashthis_s           = nextmem_d['txt']
            if new_member_d['secure_hash_ofnext']:
                hashthis_s = new_member_d['secure_hash_ofnext'] + hashthis_s
            new_member_d['secure_hash_ofnext'] = hashit(hashthis_s)
        self.head['next'] = new_member_d
        hashthis_s        = new_member_d['secure_hash_ofnext'] + new_member_d['txt']
        self.head['secure_hash_ofnext'] = hashit(hashthis_s)
        return True
    
# I should demo the Blockchain class:
blockchain = Blockchain()
blockchain.add_member(adam_d)
blockchain.add_member(eve_d)
blockchain.add_member(sam_d)
print('I should now have a blockchain.')
print(blockchain.head)

'bye'
