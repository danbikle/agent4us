"""
hash03.py

This script should demo-how-to operate a Python implementation
of a SHA-256 Cryptographic Hash Function.

python hash03.py
"""

import hashlib
"""
Ref:
https://docs.python.org/3/library/hashlib.html#simple-hashing

I refactored this syntax to create my_hashf():

>>> import hashlib
>>> m = hashlib.sha256()
>>> m.update(b"Nobody inspects")
>>> m.update(b" the spammish repetition")
>>> m.digest()
"""

def my_hashf(in_s):
    """This function should return a SHA-256 Cryptographic Hash of in_s."""
    my_hashlib = hashlib.sha256()
    in_b       = in_s.encode('utf-8')
    my_hashlib.update(in_b)
    return my_hashlib.digest()

my_in_s = "Today is Dec 27, 2017 and the weather in California is perfect."
out1_b  = my_hashf(my_in_s)
print(out1_b)

# I should try again to see if I get the same hash:
out1_b  = my_hashf(my_in_s)
print(out1_b)

my_in_s = "Boston is (16F) cold!"
out2_b  = my_hashf(my_in_s)
print(out2_b)

my_in_s = "NYC is (20F) cold too!"
out3_b  = my_hashf(my_in_s)
print(out3_b)

my_in_s = "Sydney looks comfy."
out4_b  = my_hashf(my_in_s)
print(out4_b)

'bye'
