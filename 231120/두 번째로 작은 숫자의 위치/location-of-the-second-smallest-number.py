N = int(input())
nums = list(map(int, input().split()))

num_copy = sorted(nums)

min_ = num_copy[0]
second_low_exist = False
second_low = 0
for i in range(N):
    if num_copy[i] != min_:
        second_low_exist = True
        second_low = num_copy[i]
        break

if second_low_exist == False:
    print(-1)
    exit()


ans_idx = -1
for idx, num in enumerate(nums):
    if num == second_low:
        if ans_idx != -1:
            print(-1)
            exit()

        ans_idx = idx

print(ans_idx + 1)