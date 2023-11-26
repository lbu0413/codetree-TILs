N = int(input())
arr = list(map(int, input().split()))

max_digits = 6


p = 1
for i in range(max_digits):
    tmp = [[] for _ in range(10)]
    for num in arr:
        digit = num // p % 10
        tmp[digit].append(num)
    
    arr = []
    for digit in range(10):
        for num in tmp[digit]:
            arr.append(num)
    
    p *= 10

print(*arr)