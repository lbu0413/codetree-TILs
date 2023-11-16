import sys

min_ = sys.maxsize

a, b, x, y = map(int, input().split())

option1 = b - a
option2 = min(abs(x - a) + abs(y - b), abs(x - b) + abs(y - a))

print(min(option1, option2))