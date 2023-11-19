N = int(input())

rps = [(tuple(map(int, input().split()))) for _ in range(N)]


win_one = 0
for first, second in rps:
    if first == 1 and second == 2:
        win_one += 1
    
    elif first == 2 and second == 3:
        win_one += 1
    
    elif first == 3 and second == 1:
        win_one += 1

win_two = 0

for first, second in rps:
    if first == 1 and second == 3:
        win_two += 1
    
    elif first == 3 and second == 2:
        win_two += 1
    
    elif first == 2 and second == 1:
        win_two += 1

print(max(win_one, win_two))