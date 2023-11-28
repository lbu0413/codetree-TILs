class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def empty(self):
        if not self.items:
            return 1
        else:
            return 0
    
    def pop(self):
        if self.empty():
            raise Exception("Stack is empty")
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def top(self):
        if self.empty():
            raise Exception("Stack is empty")
        return self.items[-1]

stack = Stack()

N = int(input())
for i in range(N):
    input_ = input().split()
    if len(input_) == 2:
        command = input_[0]
        num = int(input_[1])
    else:
        command = input_[0]
    
    if command == 'push':
        stack.push(num)
    
    elif command == 'top':
        print(stack.top())
    
    elif command == 'size':
        print(stack.size())
    
    elif command == 'empty':
        print(stack.empty())
    
    elif command == 'pop':
        print(stack.pop())