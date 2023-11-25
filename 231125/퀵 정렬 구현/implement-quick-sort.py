N = int(input())
arr = list(map(int, input().split()))

def quicksort(low, high):
    if low < high:
        p = partition(low, high)
        quicksort(low, p - 1)
        quicksort(p + 1, high)


def partition(low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1

quicksort(0, N-1)
print(*arr)