"""
hash03.py

This script should demo-how-to operate a popular Python implementation
of a Cryptographic Hash Function.

python hash03.py
"""
import hashlib
m = hashlib.sha256()
m.update(b"Nobody inspects")
m.update(b" the spammish repetition")
m.digest()

m.digest_size

m.block_size

