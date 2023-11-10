max_ = 1000

n, c, g, h = map(int, input().split())
ta, tb = [0] * n, [0] * n

for i in range(n):
    ta[i], tb[i] = tuple(map(int, input().split()))


def single_efficiency(low, high, t):
    if t < low:
        return c
    
    elif t <= high:
        return g
    
    else:
        return h


def work_performance(t):
    total_performance = 0
    for i in range(n):
        total_performance += single_efficiency(ta[i], tb[i], t)
    return total_performance


max_out = 0
for t in range(max_ + 1):
    max_out = max(max_out, work_performance(t))

print(max_out)