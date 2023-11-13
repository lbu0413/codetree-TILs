MAX_NUM = 10000

# 변수 선언 및 입력:
n = int(input())
conditions = [tuple(map(int, input().split()))for _ in range(n)]


for x in range(1, MAX_NUM + 1):
    tmp = x
    for a, b in conditions:
        x *= 2
        if x < a or x > b:
            break
    else:
        print(tmp)
        break