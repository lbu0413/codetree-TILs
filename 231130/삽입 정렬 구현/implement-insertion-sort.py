N = int(input())
arr = list(map(int, input().split()))


for i in range(1, N):
    j = i - 1
    tmp = arr[i]
    while j >= 0 and tmp < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    
    arr[j + 1] = tmp

print(*arr)