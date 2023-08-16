'''
Doubly linked list
'''
from Module import DoubleNode
# from Linear.Module import DoubleNode

class DoubleLinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None
    
    def append(self, item):
        new_node = DoubleNode(item)
        if self.is_empty():
            self.head = new_node
            return
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def add(self, item):
        new_node = DoubleNode(item)
        if self.is_empty():
            self.head = new_node
        new_node.next = self.head
        # self.head = new_node
    
    def insert(self, place, item):
        new_node = DoubleNode(item)
        if self.is_empty():
            return
        cur = self.head
        for i in range(1, place):
            pre = cur
            cur = cur.next
        pre.next = new_node
        new_node.next = cur
    
    def remove(self, item):
        if self.is_empty():
            return
        cur = self.head
        while cur.item != item:
            pre = cur
            cur = cur.next
        pre.next = cur.next

    def length(self):
        if self.is_empty():
            return
        size = 1
        cur = self.head
        while cur.next != None:
            cur = cur.next
            size += 1
        return size
    
    def travel(self):
        cur = self.head
        i = 0
        while cur:
            print("Element {} is {}".format(i, cur.item))
            cur = cur.next
            i += 1
    
    def search(self, item):
        if self.is_empty():
            return
        cur = self.head
        while cur.item != item and cur:
            cur = cur.next
        return cur.item == item
    
    def print_(self):
        cur = self.head
        while cur != None:
            print(cur.item)
            cur = cur.next
    

if __name__ == '__main__':
    list = DoubleLinkedList()
    for i in range(1, 9):
        list.append(i)
    list.travel()
    print(list.search(6))