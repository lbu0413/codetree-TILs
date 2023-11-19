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
distance = 0
diff2_idx = -1
if seats[0] == '0':
    for i in range(1, N):
        if seats[i] == '1':
            diff2_idx = i
            break
        distance += 1
diff2 = distance 


diff3 = -1
if seats[-1] == '0':
    for i in range(-2, -1, -1):
        if seats[i] == '1':
            break
        distance += 1
diff3 = distance


diff1 = (max_i + max_j) // 2
max_ = max((diff1), diff2, diff3)
if max_ == diff1:
    seats[diff1] = '1'

elif max_ == diff2:
    seats[0] = '1'

else:
    seats[-1] = '1'




for i in range(N):
    if seats[i] == '1':
        for j in range(i + 1, N):
            if seats[j] == '1':
                min_ = min(min_, j - i)
                break

print(min_)