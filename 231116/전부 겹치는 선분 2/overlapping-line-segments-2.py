N = int(input())

lines = [tuple(map(int, input().split())) for _ in range(N)]
ans = ""
for i in range(N):
    for j in range(N):
        if i == j:
            continue

        if not (lines[i][1] < lines[j][0]) or not (lines[j][1] < lines[i][0]):
            ans = "Yes"
            break

    else:
        ans = "No"

print(ans)