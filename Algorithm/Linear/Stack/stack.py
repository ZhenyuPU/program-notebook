'''
Stack: 后进先出(LIFO, Last In First Out)
Stack() 创建一个新的空栈
push(item) 添加一个新的元素item到栈顶
pop() 弹出栈顶元素
peek() 返回栈顶元素
is_empty() 判断栈是否为空
size() 返回栈的元素个数
'''
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):    
        return self.items == None
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)


if __name__ == '__main__':
    stack = Stack()
    stack.push("hello")
    stack.push("world")
    stack.push("itcast")
    print(stack.size())
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
        