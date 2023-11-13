import sys



N = int(input())
seats = list(input())

def distance_diff():
    min_ = sys.maxsize
    for i in range(N):
        for j in range(i + 1, N):
            if seats[i] == '1' and seats[j] == '1':
                distance = (j - i)
                min_ = min(min_, distance)
    return min_


max_ = 0
for i in range(N):
    for j in range(i + 1, N):
        if seats[i] == '0' and seats[j] == '0':
            seats[i] = '1'
            seats[j] = '1'
            max_ = max(max_, distance_diff())
            seats[i] = '0'
            seats[j] = '0'
print(max_)