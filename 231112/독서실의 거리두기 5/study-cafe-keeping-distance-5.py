import sys

max_ = -sys.maxsize

N = int(input())
library = list(input())



def closest_ones():
    closest = N
    for i in range(N):
        for j in range(i + 1, N):
            if library[i] == '1' and library[j] == '1':
                closest = min(closest, j - i)
    return closest


for i in range(N):
    if library[i] == '0':
        library[i] = '1'
        max_ = max(max_, closest_ones())

        library[i] = '0'

print(max_)