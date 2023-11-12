N = int(input())
string = input()

ans = 1

for i in range(1, N):

    twice = False

    for j in range(N - i + 1):
        for k in range(j + 1, N - i + 1):
            isSame = True

            for l in range(i):
                if string[j + l] != string[k + l]:
                    isSame = False
            
            if isSame:
                twice = True
    if twice:
        ans = i + 1
    
    else:
        break

print(ans)