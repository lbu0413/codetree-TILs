import sys

N = int(input())
seats = list(input())

min_ = sys.maxsize

max_i, max_j = -1, -1
diff = -1

for i in range(N):
    if seats[i] == '1':
        for j in range(i + 1, N):
            if seats[j] == '1':
                if j - i > diff:
                    diff = j - i
                    max_i = i
                    max_j = j
                break


diff2 = -1
max_idx = -1
if seats[0] == '0':
    distance = 0
    for i in range(N):
        if seats[i] == '1':
            diff2_idx = i
            break
        distance += 1
    
    if distance > diff2:
        diff2 = distance
        max_idx = 0


if seats[N - 1] == '0':
    distance = 0
    for i in range(N - 1, -1, -1):
        if seats[i] == '1':
            break
        distance += 1
    
    if distance > diff2:
        diff2 = distance
        max_idx = N - 1


if diff2 >= diff2 // 2:
    seats[max_idx] = '1'
else:
    seats[(max_i + max_j) // 2] = '1'


for i in range(N):
    if seats[i] == '1':
        for j in range(i + 1, N):
            if seats[j] == '1':
                min_ = min(min_, j - i)
                break

print(min_)