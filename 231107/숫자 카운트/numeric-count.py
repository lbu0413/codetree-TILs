N = int(input())

arr = [tuple(map(int, input().split())) for _ in range(N)]
# arr = [tuple(map(int, input().split()))for _ in range(n)]

ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            
            if i == j == k:
                continue

            for asked_num, cnt1, cnt2 in arr:
                c1, c2 = 0, 0
                x = asked_num // 100
                y = asked_num // 10 % 10
                z = asked_num % 10

                if i == x:
                    c1 += 1
                if j == y:
                    c1 += 1
                if k == z:
                    c1 += 1
                if j == x or y == x:
                    c2 += 1
                if i == y or i == z:
                    c2 += 1
                if k == x or k == y:
                    c2 += 1
            
                if c1 != cnt1 or c2 != cnt2:
                    break
            
            else:
                ans += 1

print(ans)