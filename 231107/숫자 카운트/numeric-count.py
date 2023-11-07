N = int(input())

arr = [tuple(map(int, input().split())) for _ in range(N)]
# arr = [tuple(map(int, input().split()))for _ in range(n)]

ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            
            if i == j or j == k or k == i:
                continue

            for asked_num, cnt1, cnt2 in arr:
                c1, c2 = 0, 0
                x = asked_num // 100
                y = asked_num // 10 % 10
                z = asked_num % 10

                if x == i:
                    c1 += 1
                if y == j:
                    c1 += 1
                if z == k:
                    c1 += 1
                if x == j or x == k:
                    c2 += 1
                if y == i or y == k:
                    c2 += 1
                if z == i or z == j:
                    c2 += 1
            
                if c1 != cnt1 or c2 != cnt2:
                    break
            
            else:
                ans += 1

print(ans)