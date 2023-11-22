N = int(input())
arr = []

for i in range(N):
    input_ = input().split()
    if len(input_) == 2:
        command = input_[0]
        num = int(input_[1])
    
    else:
        command = input_[0]

    if command == "push_back":
        arr.append(num)
    
    if command == "get":
        print(arr[num - 1])
    
    if command == "size":
        print(len(arr))

    if command == "pop_back":
        arr.pop()