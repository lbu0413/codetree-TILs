n, m, p = map(int, input().split())
p -= 1
messages = [tuple(map(str, input().split())) for _ in range(m)]

alphabets = [chr(65 + i) for i in range(n)]

people = ""
for person, number in messages:
    people += person

# 읽지 않았을 가능성이 있는 사람들 = 
# 나보다 메세지를 먼저 보낸 사람들 혹은 나 이후로 메세지를 보낸 적이 없는 사람들
suspects = []

for alph in alphabets:
    if p == 0:
        print("")
        exit()
    if alph not in people:
        suspects.append(alph)
    else:
        if people.rindex(alph) < p:
            suspects.append(alph)

print(*suspects)