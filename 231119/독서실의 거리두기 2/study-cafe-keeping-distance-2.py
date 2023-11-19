import sys

N = int(input())
seats = list(input())

min_ = sys.maxsize

max_i, max_j = 0, 0
diff = 0
if seats[-1] == '0' and seats[-2] == '0':
    seats[-1] = '1'

else:
    for i in range(N):
        if seats[i] == '1':
            for j in range(i + 1, N):
                if seats[j] == '1':
                    if j - i > diff:
                        diff = j - i
                        max_i = i
                        max_j = j
                        break
            seats[(max_i + max_j) // 2] = '1'


for i in range(N):
    if seats[i] == '1':
        for j in range(i + 1, N):
            if seats[j] == '1':
                min_ = min(min_, j - i)
                break

print(min_)