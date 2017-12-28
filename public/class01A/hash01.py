"""
hash01.py

This script should demo-how-to create a simple hash function.

Solution-Idea:
  - Get the input string, input_s
  - Maybe the string is too short
  - add a 256 bit string to end of input_s 
  - return first 256 bits of input_s

Note that I can create 256 bits from 32 characters which are 8 bytes each.

Demo:
python hash01.py
"""

def my_hashf(in_s):
    """This function should combine in_s with 256 bits."""
    pad64_s = "01234567" # This is 8 utf-8 characters which is 64 bits.
    # 256 / 64 is 4
    pad256_s = pad64_s + pad64_s + pad64_s + pad64_s
    out_s = in_s + pad256_s
    # I should return the first 256 bits of out_s.
    # 256 bits is 32 bytes; I should return the first 32 bytes:
    return out_s[0:32]

my_in_s = "Today is Dec 27, 2017 and the weather in California is perfect."
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
