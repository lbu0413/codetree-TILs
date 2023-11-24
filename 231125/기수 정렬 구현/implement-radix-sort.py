N = int(input())
arr = list(map(int, input().split()))

MAX_K = 6
MAX_DIGIT = 10

def radix_sort():
    global arr

    p = 1
    for pos in range(MAX_K):
        new_arr = [[] for _ in range(MAX_DIGIT)]
        for elem in arr:
            digit = (elem // p) % 10
            new_arr[digit].append(elem)
        
        arr = []
        for digit in range(MAX_DIGIT):
            for elem in new_arr[digit]:
                arr.append(elem)
        
        p *= 10

radix_sort()

print(*arr)