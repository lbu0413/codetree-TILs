a, b = map(int, input().split())


def prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


total = 0
for i in range(a, b + 1):
    if i == 1:
        print(0)
        exit()
    if prime(i):
        total += i

print(total)