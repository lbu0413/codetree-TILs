N = int(input())

rps = [(tuple(map(int, input().split()))) for _ in range(N)]


first_max = 0
second_max = 0
for first, second in rps:
    if first == second:
        continue
    
    if first == 1 and second == 2:
        first_max += 1
    
    elif first == 2 and first == 1:
        second_max += 1
    
    elif first == 1 and second == 3:
        second_max += 1
    
    elif first == 3 and second == 1:
        first_max += 1
    
    elif first == 2 and second == 3:
        first_max += 1
    
    elif first == 3 and second == 2:
        second_max += 1

print(max(first_max, second_max))