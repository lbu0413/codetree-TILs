import sys

nums = list(map(int, input().split()))

MAX_I = 40
MAX_N = 15


for a in range(1, MAX_I + 1):
    for b in range(1, MAX_I + 1):
        for c in range(1, MAX_I + 1):
            for d in range(1, MAX_I + 1):
                arr2 = [a, b, c, d, a+b, b+c, c+d, d+a, a+c, b+d, a+b+c, a+b+d, a+c+d, b+c+d, a+b+c+d]
                if sorted(arr2) == sorted(nums):
                    print(a, b, c, d)
                    sys.exit(0)