N = int(input())
nums = list(map(int, input().split()))

tmp = sorted(nums.copy())
min_ = tmp[0]

for i in range(1, len(tmp)):
    if tmp[i] > min_:
        if nums.count(tmp[i]) > 1:
            print(-1)
            exit()
        print(nums.index(tmp[i]) + 1)
        break

else:
    print(-1)