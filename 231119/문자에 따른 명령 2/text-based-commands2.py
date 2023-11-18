direction = list(input())
N = len(direction)

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
direction_num = 3

x, y = 0, 0
for i in direction:
    if i == 'L':
        direction_num = (direction_num - 1 + 4) % 4
    
    elif i == 'R':
        direction_num = (direction_num + 1) % 4
    
    else:
        x = x + dx[direction_num]
        y = y + dy[direction_num]

print(x, y)