"""
~/cryp4/public/class01A/hash_afile.py

This script should calculate a SHA-256 'secure-hash' of a large file. 

Ref:
http://cryp4.us/cclasses/class01A#compare2
https://www.google.com/search?q=how+to+Use+Python+to+get+calculate+a+SHA-256+hash-digest+of+a+large+file
https://gist.github.com/aunyks/042c2798383f016939c40aa1be4f4aaf

Demo:
python hash_afile.py
"""

import hashlib
import os

# I should use curl to get a large file:
curl   = '/usr/bin/curl '
my_url = 'https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh '
largef = '/tmp/Anaconda3-5.0.1-Linux-x86_64.sh'
# I should use Python to run a shell command:
os.system(curl + my_url + '>' + largef)

# Specify how many bytes of the file you want to open at a time
blocksize_i = 2**16

# I should access the SHA-256 algo:
my_hashlib  = hashlib.sha256()

with open(largef, 'rb') as large_fh:
    file_buffer = large_fh.read(blocksize_i)
    while len(file_buffer) > 0:
        my_hashlib.update(file_buffer)
        file_buffer = large_fh.read(blocksize_i)
        
print('my_hashlib.hexdigest() of ')
print(largef, ' is: ')
print(my_hashlib.hexdigest())

'bye'
