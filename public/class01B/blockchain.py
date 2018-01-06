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

# I should create my first member of the linked-list:
adam_d = {'txt': 'Genesis says Adam is here.'}
# I should create more members:
eve_d = {'txt': 'Eve says Hi.'}
sam_d = {'txt': 'Sam is short for either Samantha or Samuel.'}
# I have members but they are not linked yet.

class Blockchain():
    """Class for creating a data structure called a 'Linked-List'."""
    def __init__(self):
        self.head = {'list_head': True, 'next': None, 'secure_hash_ofnext': None}
    def add_member(self, new_member_d):
        new_member_d['next'] = self.head['next']
        # I should calculate secure_hash_ofnext
        # which should be hash of next txt-value
        # and hash of next secure_hash_ofnext-value.
        self.head['next'] = new_member_d
        return True
    
# I should demo the Blockchain class:
blockchain = Blockchain()
blockchain.add_member(adam_d)
blockchain.add_member(eve_d)
blockchain.add_member(sam_d)
print('I should now have a blockchain.')
print(blockchain.head)

'bye'
