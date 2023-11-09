gh = list(input())

cnt = 0
for i in range(len(gh)):
    for j in range(i+1, len(gh)):
        if gh[i] == '(' and gh[j] == ')':
            cnt += 1

print(cnt)