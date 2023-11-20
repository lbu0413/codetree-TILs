N = int(input())
nums = list(map(int, input().split()))

tmp = sorted(nums.copy())
min_ = tmp[0]

for i in range(1, len(tmp)):
    if tmp[i] > min_:
        print(nums.index(tmp[i]) + 1)
        break

else:
    print(-1)