N = int(input())
arr = list(map(int, input().split()))

def partition(left, right):
    pivot = arr[right]
    i = left - 1

    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1



def quick_sort(left, right):
    if left < right:
        p = partition(left, right)
        quick_sort(left, p - 1)
        quick_sort(p + 1, right)

quick_sort(0, N-1)
print(*arr)