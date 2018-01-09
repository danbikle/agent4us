"""~/cryp4/public/class01B/blockchain.py

This script should demo how to create a very simple Blockchain with Python.

The Blockchain class will be similar to the LinkedList class I
demonstrated earlier.

But each element, a simple dictionary, has an additional attribute called
secure_hash_ofnext.

Additionally, Blockchain has a Boolean class-method named isvalid().

The isvalid() method should return True as I build the blockchain.

It should return False later, if I change data in the blockchain.

Demo:
python blockchain.py
"""

import hashlib
import pdb

# I should create my first member of the linked-list:
adam_d = {'txt': 'Genesis says Adam is here.'}
# I should create more members:
eve_d = {'txt': 'Eve says Hi.'}
sam_d = {'txt': 'Sam is short for either Samantha or Samuel.'}
# I have members but they are not linked yet.

class Blockchain():
    """Class for creating a data structure called a 'Blockchain'."""
    def __init__(self):
        """I should create a dictionary which gets the structure started in a nice state."""
        self.head = {'list_head': True, 'next': None, 'secure_hash_ofnext': None, 'txt': None}
        
    def hashit(self, in_b):
        """This should transform in_b into a SHA-256 secure-hash."""
        # I prefer in_b to be encoded as 'utf-8'.
        my_hashlib = hashlib.sha256()
        my_hashlib.update(in_b)
        return my_hashlib.digest()

    def hash2em(self, elem_d):
        """This should return a secure hash of """
        """either some text or a secure-hash concatenated to some text."""
        if ('secure_hash_ofnext' not in elem_d) or (elem_d['secure_hash_ofnext'] == None):
            # if elem_d has no secure_hash_ofnext, do this:
            hashthis_s = elem_d['txt'].encode('utf-8')
        else:
            hashthis_s = elem_d['secure_hash_ofnext'] + elem_d['txt'].encode('utf-8')
        return self.hashit(hashthis_s)
        
    def isvalid(self, current_d=None):
        """This should return True if blockchain is valid."""
        # I intend to operate this method recursively.
        if current_d == None:
            # I should land here during initial call:
            current_d = self.head
        if current_d['next'] == None:
            return True # This s.b. happy-path-exit
        if (current_d['secure_hash_ofnext'] != self.hash2em(current_d['next'])):
            return False # I should exit here if blockchain invalid.
        else:
            # I should recurse to look at the next element in the blockchain:
            return self.isvalid(current_d['next'])
    
    def add_member(self, new_member_d):
        """This should add a member from a properly formatted dictionary."""
        new_member_d['next']               = self.head['next']
        new_member_d['secure_hash_ofnext'] = self.head['secure_hash_ofnext']
        self.head['next']                  = new_member_d
        self.head['secure_hash_ofnext']    = self.hash2em(new_member_d)
        return True
    
# I should demo the Blockchain class:
blockchain = Blockchain()
print(blockchain.isvalid()) # s.b. True
blockchain.add_member(adam_d)
print(blockchain.isvalid()) # s.b. True
blockchain.add_member(eve_d)
print(blockchain.isvalid()) # s.b. True
blockchain.add_member(sam_d)
print('I should now have a blockchain.')
print(blockchain.head)
print(blockchain.isvalid()) # s.b. True
i_am_eve_d = blockchain.head['next']['next']
i_am_eve_d['txt'] = 'Eve says hello.'
print(blockchain.isvalid()) # s.b. False
i_am_eve_d['txt'] = 'Eve says Hi.'
print(blockchain.isvalid()) # s.b. True

'bye'
