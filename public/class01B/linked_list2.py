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
# I have members but they are not linked yet.

class LinkedList():
    """Class for creating a data structure called a 'Linked-List'."""
    def __init__(self):
        self.head = {'list_head': True, 'next': False}
    def add_member(self, new_member_d):
        new_member_d['next'] = self.head['next']
        self.head['next']    = new_member_d
        return True
    
# I should demo the LinkedList class:
linked_list = LinkedList()
linked_list.add_member(adam_d)
linked_list.add_member(eve_d)
linked_list.add_member(sam_d)
# I should see it:
print(linked_list.head)

'bye'
