import sys

n, m, p = map(int, input().split())
messages = [tuple(map(str, input().split())) for _ in range(m)]


if int(messages[p - 1][1]) == 0:
    sys.exit()

for i in range(n):
    person = chr(ord('A') + i)
    read = False

    for c, u in messages:
        u = int(u)
        if u >= int(messages[p - 1][1]) and c == person:
            read = True
        
    
    if read == False:
        print(person, end=" ")