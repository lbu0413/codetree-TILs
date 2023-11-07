import sys

max_ = -sys.maxsize
min_ = sys.maxsize

developers = list(map(int, input().split()))
N = 5

def duplicates(i, j, k, l):
    team1 = developers[i] + developers[j]
    team2 = developers[k] + developers[l]
    team3 = sum(developers) - (team1 + team2)

    if team1 == team2 or team1 == team3 or team2 == team3:
        return True
    
    return False


def get_diff(i, j, k, l):
    team1 = developers[i] + developers[j]
    team2 = developers[k] + developers[l]
    team3 = sum(developers) - (team1 + team2)
    
    max_team = max(team1, team2, team3)
    min_team = min(team1, team2, team3)

    return max_team - min_team


for i in range(N):
    for j in range(i+1, N):
        for k in range(N):
            for l in range(k+1, N):
                if i == k or i == l or j == k or j == l:
                    continue
                if duplicates(i, j, k, l):
                    continue
                diff_ = get_diff(i, j, k, l)
                min_ = min(min_, diff_)

print(min_)