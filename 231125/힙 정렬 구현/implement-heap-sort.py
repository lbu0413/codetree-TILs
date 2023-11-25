N = int(input())
arr = list(map(int, input().split()))


def heapify(N, i):
    largest = i
    left = i * 2
    right = i * 2 + 1

    if left < N and arr[left] > arr[largest]:
        largest = left
    
    if right < N and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(N, largest)

def heapsort():
    for i in range(N//2, -1, -1):
        heapify(N, i)
    
    for i in range(N-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(i, 0)
        

heapsort()

print(*arr)