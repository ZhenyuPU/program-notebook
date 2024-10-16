'''
双端队列(deque，全名double-ended queue)，是一种具有队列和栈的性质的数据结构。
双端队列中的元素可以从两端弹出，其限定插入和删除操作在表的两端进行。双端队列可以在队列任意一端入队和出队。

Deque() 创建一个空的双端队列
add_front(item) 从队头加入一个item元素, 队头固定，但是元素进入队尾那里
add_rear(item) 从队尾加入一个item元素
remove_front() 从队头删除一个item元素
remove_rear() 从队尾删除一个item元素
is_empty() 判断双端队列是否为空
size() 返回队列的大小
'''

class Deque:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)
    
    def remove_front(self):
        return self.items.pop(0)
    
    def remove_rear(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    

if __name__ == "__main__":
    deque = Deque()
    deque.add_front(1)
    deque.add_front(2)
    deque.add_rear(3)
    deque.add_rear(4)
    print(deque.size())
    print(deque.remove_front())
    print(deque.remove_front())
    print(deque.remove_rear())
    print(deque.remove_rear())