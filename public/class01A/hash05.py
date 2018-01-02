"""
hash05.py

This script should demo-how-to operate a Python implementation
of a SHA-256 Cryptographic Hash Function.

Demo:
python hash05.py

Ref:
https://docs.python.org/3/library/hashlib.html#simple-hashing

The function, my_hashf() below, was created after I refactored this
syntax from the above web page:

>>> import hashlib
>>> m = hashlib.sha256()
>>> m.update(b"Nobody inspects")
>>> m.update(b" the spammish repetition")
>>> m.digest()

"""

import hashlib

def my_hashf(in_s):
    """This function should return a SHA-256 Cryptographic Hash of in_s."""
    my_hashlib = hashlib.sha256()
    in_b       = in_s.encode('utf-8')
    my_hashlib.update(in_b)
    # I should convert it to a readable string:
    digest_s = my_hashlib.hexdigest().upper()
    return digest_s

my_in_s         = "123456"
digest_of123456 = my_hashf(my_in_s)
# s.b.
# 8D969EEF6ECAD3C29A3A629280E686CF0C3F5D5A86AFF3CA12020C923ADC6C92
print(digest_of123456)
print('The Java-app gave this value:')
print('8D969EEF6ECAD3C29A3A629280E686CF0C3F5D5A86AFF3CA12020C923ADC6C92')

print('I will hash more strings now:')

my_in_s = "Today is Dec 27, 2017 and the weather in California is perfect."
out1_s  = my_hashf(my_in_s)
print(out1_s)

# I should try again to see if I get the same hash:
out1_s  = my_hashf(my_in_s)
print(out1_s)

my_in_s = "Boston is (16F) cold!"
out2_s  = my_hashf(my_in_s)
print(out2_s)

my_in_s = "NYC is (20F) cold too!"
out3_s  = my_hashf(my_in_s)
print(out3_s)

my_in_s = "Sydney looks comfy."
out4_s  = my_hashf(my_in_s)
print(out4_s)

'bye'
