a, b = map(int, input().split())

interesting_num_cnt = 0
for i in range(a, b+1):
    num = i
    checker = [0] * 10
    digit_cnt = 0
    while num:
        checker[num % 10] += 1
        digit_cnt += 1
        num = num // 10
    
    interesting_num = False
    for j in range(10):
        if checker[j] == digit_cnt - 1:
            interesting_num = True
    
    if interesting_num:
        interesting_num_cnt += 1

print(interesting_num_cnt)