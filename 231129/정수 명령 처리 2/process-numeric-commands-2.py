from collections import deque


class Queue:
    def __init__(self):
        self.dq = deque()
    
    def push(self, item):
        self.dq.append(item)
    
    def pop(self):
        if not self.dq:
            raise Exception("Queue is empty")
        else:
            return self.dq.popleft()
    
    def size(self):
        return len(self.dq)
    
    def empty(self):
        if len(self.dq) == 0:
            return 1
        else:
            return 0
    
    def front(self):
        if not self.dq:
            raise Exception("Queue is empty")
        else:
            return self.dq[0]

q = Queue()
N = int(input())
for i in range(N):
    input_ = input().split()
    if len(input_) == 2:
        command = input_[0]
        num = input_[1]
    else:
        command = input_[0]
    
    if command == "push":
        q.push(num)
    
    elif command == "front":
        print(q.front())
    
    elif command == "size":
        print(q.size())
    
    elif command == "empty":
        print(q.empty())
    
    elif command == "pop":
        print(q.pop())