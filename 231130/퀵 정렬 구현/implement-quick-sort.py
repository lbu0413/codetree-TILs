N = int(input())
arr = list(map(int, input().split()))


def quick_sort(low, high):
    if low < high:
        p = partition(low, high)
        quick_sort(low, p - 1)
        quick_sort(p + 1, high)


def partition(low, high):
    pivot = arr[high]
    j = low - 1

    for i in range(low, high):
        if arr[i] < pivot:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[j + 1], arr[high] = arr[high], arr[j + 1]

    return j + 1


quick_sort(0, N-1)
print(*arr)