"""
puzzle_solve.py

This script should solve a puzzle using a "Puzzle Friendly"
Cryptographic Hash function named SHA-256.

The idea is very simple; this script should 'search' for an integer in a range.

The approach will be simple: start at zero and try each integer in the range.

Demo:
python puzzle_solve.py
"""

import hashlib

# I should find the integer, between 0 through 1e+4, which gives this hash-digest via SHA-256:
puzzle_digest_s = '02BE6761F02F2291C1FE54C103440F7B9BA65DA74DC84F1E08736D7A67824643'

# I should start solving by specifying a range of integers.
# If the range is large, the puzzle will be difficult.
range_i  = int(1e+4)

for int_i in range(range_i+1):
    # I should convert the number to a string and feed that string to SHA-256:
    in_s       = str(int_i)
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
    if (digest_s == puzzle_digest_s):
        print('I solved the puzzle. The integer is: ',int_i)
        break
'bye'
