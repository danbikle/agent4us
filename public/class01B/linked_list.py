"""
~/cryp4/public/class01B/linked_list.py

This script should demo how to create a linked list with Python.

Each member of the linked list should be a simple dictionary.

I should add members to the head of the linked list instead of the end.
So, older members should be at the end.

Demo:
python linked_list.py
"""

# I should create the head of the list:
list_head_d = {'list_head': True}

# I should create my first member of the linked-list:
adam_d      = {'txt': 'Genesis says Adam is here.'}
# I should update the head of the list:
list_head_d['next'] = adam_d

# I should create another member:
eve_d = {'txt': 'Eve says Hi.'}
# I should create a link.
# Should Adam point to Eve?
# Should Eve point to Adam?
# What should change? older element or newer element?
# I think that newer element should be more changeable.
eve_d['next'] = adam_d
# I should update the head of the list:
list_head_d['next'] = eve_d

# Can I print this?
print(list_head_d)

# I should create another member:
sam_d = {'txt': 'Sam is short for either Samantha or Samuel.'}
sam_d['next']       = eve_d
list_head_d['next'] = sam_d
print(list_head_d)

print('I should now have a linked list.')
print(list_head_d['next'] == sam_d)
print(sam_d['next']       == eve_d)
print(eve_d['next']       == adam_d)

'bye'
