N = int(input())
arr = list(map(int, input().split()))

def merge_sort(left, right):
    mid = (left + right) // 2
    if left < right:
        merge_sort(left, mid)
        merge_sort(mid+1, right)
        merge(left, mid, right)

sorted_arr = [0] * N
def merge(left, mid, right):
    first = left
    second = mid + 1
    idx = left
    
    while first <= mid and second <= right:
        if arr[first] <= arr[second]:
            sorted_arr[idx] = arr[first]
            first += 1
            idx += 1
        
        else:
            sorted_arr[idx] = arr[second]
            second += 1
            idx += 1
    
    while first <= mid:
        sorted_arr[idx] = arr[first]
        first += 1
        idx += 1
    
    while second <= right:
        sorted_arr[idx] = arr[second]
        second += 1
        idx += 1
    
    for k in range(left, right + 1):
        arr[k] = sorted_arr[k]
    



merge_sort(0, N-1)
print(*arr)