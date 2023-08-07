'''
Definitions of node and double node as follows
'''

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

    def __str__(self):
        return str(self.item)