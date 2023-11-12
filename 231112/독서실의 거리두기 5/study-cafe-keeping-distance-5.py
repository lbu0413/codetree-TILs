N = int(input())
seats = list(input())


def find_closest():
    min_ = N
    for i in range(N):
        for j in range(i + 1, N):
            if seats[i] == '1' and seats[j] == '1':
                min_ = min(min_, j - i)
    
    return min_

ans = 0
for i in range(N):
    if seats[i] == '0':
        seats[i] = '1'
        ans = max(ans, find_closest())
        seats[i] = '0'

print(ans)