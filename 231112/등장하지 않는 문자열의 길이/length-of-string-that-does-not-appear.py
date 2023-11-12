MAX = 100 + 1

N = int(input())
str_input = list(input())

cnt = 0
for i in range(1, MAX):
    for j in range(0, N, i):
        for k in range(j + 1, N, i):
            if str_input[j] == str_input[k]:
                cnt += 1

print(cnt)