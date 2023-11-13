a, b = map(int, input().split())

def include(num):
    while num > 0:
        res = num % 10
        num //= 10
        if res == 3 or res == 6 or res == 9:
            return True
    return False

def multiple(num):
    if num % 3 == 0:
        return True
    return False

cnt = 0
for i in range(a, b+1):
    if include(i) or multiple(i):
        cnt += 1

print(cnt)