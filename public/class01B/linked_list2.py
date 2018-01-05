"""
~/cryp4/public/class01B/linked_list2.py

This script should demo how to create a linked list with Python.

Each member of the linked list should be a simple dictionary.

I should add members to the head of the linked list instead of the end.
So, older members should be at the end.

The linked list should be a class named LinkedList which has method: add_member.

Demo:
python linked_list2.py
"""

# I should create my first member of the linked-list:
adam_d = {'txt': 'Genesis says Adam is here.'}
# I should create more members:
eve_d = {'txt': 'Eve says Hi.'}
sam_d = {'txt': 'Sam is short for either Samantha or Samuel.'}

def nnew():
    return {'list_head': True, 'next': False}

# I should create the head of the list:
list_head_d = nnew()

def add_member(list_head_d, new_member_d):
    new_member_d['next'] = list_head_d['next']
    list_head_d['next']  = new_member_d
    return True

add_member(list_head_d, adam_d)
add_member(list_head_d, eve_d)
add_member(list_head_d, sam_d)
print(list_head_d)


'bye'
