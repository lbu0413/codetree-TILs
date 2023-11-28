gh = list(input())

stack = []

for i in gh:
    if i == "(":
        stack.append(i)
    
    else:
        if len(stack) == 0:
            print("No")
            exit()
        
        elif stack[-1] == ")":
            print("No")
            exit()
        
        else:
            stack.pop()

if len(stack) != 0:
    print("No")

else:
    print("Yes")