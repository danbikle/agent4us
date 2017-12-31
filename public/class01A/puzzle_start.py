"""
puzzle_start.py

This script should start a puzzle using a "Puzzle Friendly"
Cryptographic Hash function named SHA-256.

The idea is very simple; this script should pick a random integer.

Later a contestant will solve the puzzle by guessing the random integer.

Demo:
python puzzle_start.py
"""

import hashlib
import secrets

# I should start puzzle creation by specifying a range of integers.
# If the range is large, the puzzle will be difficult.
range_i  = int(1e+4)
# I should pick a random number from the range:
random_i = secrets.choice(range(range_i))
# I should convert the number to a string and feed that string to SHA-256:
in_s       = str(random_i)
my_hashlib = hashlib.sha256()
my_hashlib.update(in_s.encode('utf-8'))
digest_b = my_hashlib.digest()
# I should convert hashdigest_b to a string:
digest1_s_l = [] # I should fill this with loop below:
for digest_i in digest_b:
    digest0_s = hex(digest_i)
    digest1_s = digest0_s.replace('x','')[-2:]
    digest1_s_l.append(digest1_s)
# I should convert digest1_s_l to a string:
digest_s = ''.join(digest1_s_l).upper()
print("You should publish this SHA-256 hash-digest.")
print("Ask contestants to find the integer which created this digest:")
print(digest_s)
print("Here is the secret integer you want them to find:")
print(random_i)

'bye'
