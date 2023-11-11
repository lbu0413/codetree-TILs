import sys

max_ = -sys.maxsize

a, b, c = map(int, input().split())


for i in range(c // a + 1):
    a_val = a * i
    b_cnt = (c - a_val) // b
    current = (a_val) + (b_cnt * b)
    max_ = max(max_, current)

print(max_)