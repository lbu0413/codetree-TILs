N = int(input())
arr = list(map(int, input().split()))

def merge_sort(arr, low, high):
    if len(arr) == 1:
        return
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        merge(arr, low, mid, high)
    return arr

sorted_arr = [0] * N
def merge(arr, low, mid, high):
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
    

print(*merge_sort(arr, 0, N-1))