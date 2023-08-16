'''
single LinkedList:
Definition
Insert
Delete
Check if full
Search
Print
It is impossible that node.next.item because node.next is not attribute Node
'''
from Module import Node

class SingleLinkedList:
    def __init__(self, limit):
        self.head = None
        self.size = 1
        self.limit = limit + 1   # Remain a place for a sentry

    def insert(self, node: Node, item, place):
        if self.size >= self.limit:
            raise IndexError("List is full")
        elif place == 1:
            new_node = Node(item)
            new_node.next = node
            node = new_node
        else:
            place -= 1
            node.next = self.insert(node.next, item, place)
        return node
            

    def is_Full(self):
        return self.size >= self.limit
    
    def is_empty(self, list: Node):
        return list is None
    
    def delete(self, item):
        if self.is_empty(self.head):
            return
        cur = self.head
        while cur.item != item:   
            pre = cur
            cur = cur.next
        pre.next = cur.next
        self.size -= 1

    def length(self):
        pre_head = self.head
        while pre_head.next:
            self.size += 1
            pre_head = pre_head.next
        return self.size - 1
    
    def search(self, node):
        pre_head = self.head
        while pre_head != node:
            pre_head = pre_head.next
        return bool(pre_head)
    
    def append(self, item):
        new_node = Node(item)
        cur = self.head
        if self.is_empty(self.head):
            self.head = new_node
        else:
            while cur.next:
                cur = cur.next
            cur.next = new_node
    '''
    在单链表中，要添加新节点，你应该在链表末尾节点的 next 指针处添加新节点
    These codes are wrong because the attribut of node.next in python cannot be fixed. In that case we use None to represent node.next.
    And here I don't connect cur with cur.next but just make cur a new node.
    In fact we need to make the end of cur point to new_node.
    Here is a wrong example:
    '''
    def append2(self,item):
        new_code = Node(item)
        cur = self.head
        displayf(self.head)
        while cur:
            cur = cur.next 
        cur = new_code
    
    def printf(self, node: Node):
        if self.is_empty(node):
            print(None)
            return
        else:
            print(node.item)
            self.printf(node.next)

    def display(self):
        cur = self.head
        if self.is_empty(cur):
            return
        else:
            while cur:
                print(cur.item)
                cur = cur.next
            print("None")  


def displayf(list: Node):
    cur = list
    if not list:
        print("none of list")
    else:
        while cur:
            print(cur.item)
            cur = cur.next
        print("None")         
    
if __name__ == '__main__':
    node = SingleLinkedList(100)
    node1 = SingleLinkedList(100)
    for i in range(6):
        node.append(i)
    node.size = node.length() 
    #node.display()
    #node.printf(node.head)
    #node.insert(node.head, 18, 4)
    #node.printf(node.head)
    for i in range(2,9):
        node1.append2(i)
    #displayf(node1.head)