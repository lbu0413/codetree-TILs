import sys

max_ = -sys.maxsize
N, B = map(int, input().split())
presents = sorted([tuple(map(int, input().split())) for _ in range(N)])

for i in range(N): # 쿠폰을 쓸 선물을 고른다
    gift, shipping = presents[i]
    gift = gift // 2
    total = gift + shipping
    cnt = 1
    for j in range(N):
        if i == j:
            continue
        if total + presents[j][0] + presents[j][1] <= B:
            total += presents[j][0] + presents[j][1]
            cnt += 1
    max_ = max(max_, cnt)
        


print(max_)