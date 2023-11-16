n, m, p = map(int, input().split())
messages = [tuple(map(str, input().split())) for _ in range(m)]
alphabets = [chr(65 + i) for i in range(n)]
p = p - 1

people = ""
for a, b in messages:
    people += a

# 읽지 않았을 가능성이 있는 사람들 = 
# 나보다 메세지를 먼저 보낸 사람들 혹은 나 이후로 메세지를 보낸 적이 없는 사람들

if p == 0:
    print("")
    exit()

suspects = []
for i in range(n):
    if alphabets[i] not in people:
        suspects.append(alphabets[i])

    elif messages[i][1] == messages[p][1]:
        continue
    
    elif people.rindex(messages[i][0]) < p:
        suspects.append(messages[i][0])
        
    
    
print(*sorted(suspects))