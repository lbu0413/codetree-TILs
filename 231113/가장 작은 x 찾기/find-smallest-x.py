MAX_NUM = 10000

# 변수 선언 및 입력:
n = int(input())
conditions = [tuple(map(int, input().split()))for _ in range(n)]

def satisfy(x):
    for a, b in conditions:
        x *= 2
        if not (a <= x <= b):
            return False
    return True


for x in range(1, MAX_NUM + 1):
    if satisfy(x):
        print(x)
        break