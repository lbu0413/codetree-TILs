N, M = map(int, input().split())
nums = list(map(int, input().split()))


# 와이파이 한 대가 커버할 수 있는 범위
cover = 2 * M + 1

if M == 0:
    print(nums.count(1))

elif N == nums.count(0):
    print(0)


else:
    if cover >= N:
        ans = 1
    else:
        ans = N // cover + N % cover

    print(ans)