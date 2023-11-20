N = int(input())

A, B = 0, 0
leader = ""

number_of_changes = 0

for i in range(N):
    tmp_leader = ""
    person, score_change = map(str, input().split())
    score_change = int(score_change)

    if person == 'A':
        A += score_change
    
    if person == 'B':
        B += score_change
    
    if A > B:
        tmp_leader = 'A'
    
    elif B > A:
        tmp_leader = 'B'
    
    if tmp_leader != leader:
        number_of_changes += 1
        leader = tmp_leader
    

print(number_of_changes)