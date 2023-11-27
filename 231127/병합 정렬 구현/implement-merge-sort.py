N = int(input())
arr = list(map(int, input().split()))

sorted_arr = [0] * N

def merge_sort(left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(left, mid)
        merge_sort(mid + 1, right)
        merge(left, mid, right)
    

def merge(left, mid , right):
    first = left
    second = mid + 1
    third = left

    while first <= mid and second <= right:
        if arr[first] <= arr[second]:
            sorted_arr[third] = arr[first]
            first += 1
            third += 1
        
        else:
            sorted_arr[third] = arr[second]
            second += 1
            third += 1
    
    while first <= mid:
        sorted_arr[third] = arr[first]
        first += 1
        third += 1
    
    while second <= right:
        sorted_arr[third] = arr[second]
        second += 1
        third += 1
    
    for i in range(left, right + 1):
        arr[i] = sorted_arr[i]

merge_sort(0, N - 1)
print(*arr)