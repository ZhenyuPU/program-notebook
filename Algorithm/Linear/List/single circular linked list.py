'''
single circular linked list
self.head is a reference to an empty singly linked list, it is not a false value
range doesn't include last element
'''
from Module import Node
class SingleCycleLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.head.next = self.head

    def is_empty(self):
        return self.head.next == self.head

    def append(self, item):
        new_node = Node(item)
        if not self.head.item:
            self.head.item = new_node
            new_node.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def remove(self, item):
        cur = self.head
        while cur.item != item:
            pre = cur
            cur = cur.next
        if cur.next == self.head:  # The item is the last node
            pre.next = self.head
        elif cur == self.head:  # The item is the head node
            last = self.head
            while last.next != self.head:
                last = last.next
            last.next = self.head.next
        else:
            pre.next = cur.next

    def insert(self, place, item):
        new_node = Node(item)
        if self.is_empty():
            return
        cur = self.head
        if place == 1:
            last = self.head
            while last.next != self.head:
                last = last.next
            last.next = new_node
            new_node.next = self.head
        else:
            for i in range(1, place):
                pre = cur
                cur = cur.next
            pre.next = new_node
            new_node.next = cur

    def search(self, item):
        if self.is_empty():
            return False
        cur = self.head.next
        while cur.item != item and cur != self.head:
            cur = cur.next
        return bool(cur.item == item)

    def print_(self):
        if self.is_empty():
            return
        cur = self.head.next
        print(self.head.item)
        while cur != self.head:
            print(cur.item)
            cur = cur.next


if __name__ == '__main__':
    alist = SingleCycleLinkedList()
    for i in range(1, 9):
        alist.append(i)
    alist.print_()
    print(alist.search(1))