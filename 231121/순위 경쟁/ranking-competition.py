N = int(input())
A, B, C = 0, 0, 0
leader = ""
cnt = 0

for i in range(N):
    person, score = map(str, input().split())
    score = int(score)

    if person == 'A':
        A += score
    
    if person == 'B':
        B += score
    
    if person == 'C':
        C += score
    
    current_max = max(A, B, C)
    
    if current_max == A == B == C:
        continue
    
    if current_max == A and leader != 'A':
        cnt += 1
        leader = 'A'
    
    elif current_max == B and leader != 'B':
        cnt += 1
        leader = 'B'
    
    elif current_max == C and leader != 'C':
        cnt += 1
        leader = 'C'

print(cnt)