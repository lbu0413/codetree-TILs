from collections import deque


dq = deque()

N = int(input())
for i in range(N):
    input_ = input().split()
    if len(input_) == 2:
        command = input_[0]
        num = input_[1]
    
    else:
        command = input_[0]
    
    if command == 'push_back':
        dq.append(num)
    
    elif command == 'push_front':
        dq.appendleft(num)
    
    elif command == 'pop_front':
        print(dq.popleft())
    
    elif command == 'front':
        print(dq[0])
    
    elif command == 'pop_back':
        print(dq.pop())
    
    elif command == 'back':
        print(dq[-1])
    
    elif command == 'size':
        print(len(dq))
    
    elif command == 'empty':
        print(0 if dq else 1)