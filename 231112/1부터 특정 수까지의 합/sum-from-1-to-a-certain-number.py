N = int(input())

def returner(num):
    sum_ = 0
    for i in range(1, num+1):
        sum_ += i
    
    return sum_ // 10

print(returner(N))