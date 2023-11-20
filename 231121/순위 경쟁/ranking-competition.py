N = int(input())

scores = [tuple(map(str, input().split())) for _ in range(N)]
a, b, c = 0, 0, 0

number_of_leader_change = 0
def get_scores(a, b, c):
    if a > b and a > c: # A가 리더인 경우
        return 1
    
    elif b > a and b > c: # B가 리더인 경우
        return 2
    
    elif c > a and c > b: # c가 리더인 경우
        return 3

    elif a == b == c:
        return 4
    
    elif a == b:
        return 5
    
    elif a == c:
        return 6
    
    elif b == c:
        return 7


for person, score in scores:
    score = int(score)

    if person == 'A':
        if get_scores(a, b, c) != get_scores(a + score, b, c):
            number_of_leader_change += 1
        a += score
    
    elif person == 'B':
        if get_scores(a, b, c) != get_scores(a, b + score, c):
            number_of_leader_change += 1
        b += score
    
    else:
        if get_scores(a, b, c) != get_scores(a, b, c + score):
            number_of_leader_change += 1
        c += score

print(number_of_leader_change)