N = int(input())
arr = list(map(int, input().split()))

def merge_sort(low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(low, mid)
        merge_sort(mid+1, high)
        merge(low, mid, high)

sorted_arr = [0] * N
def merge(low, mid, high):
    i = low
    j = mid + 1
    k = low
    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            sorted_arr[k] = arr[i]
            i += 1
            k += 1
        
        else:
            sorted_arr[k] = arr[j]
            j += 1
            k += 1
    
    while i <= mid:
        sorted_arr[k] = arr[i]
        i += 1
        k += 1
    
    while j <= high:
        sorted_arr[k] = arr[j]
        j += 1
        k += 1

    for x in range(low, high + 1):
        arr[x] = sorted_arr[x]
    

merge_sort(0, N-1)

print(*arr)