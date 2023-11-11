MAX_A = 3
MAX_X = 9

ttt = [list(map(int, input())) for _ in range(MAX_A)]
ans = 0

for i in range(1, MAX_X + 1):
    for j in range(1, MAX_X + 1):
        if i == j:
            break
        num_i, num_j = 0, 0
        win = False
    
        # 가로로 한 줄을 맞췄을 때
        for k in range(MAX_A):
            num_i, num_j = 0, 0
            for l in range(MAX_A):
                if ttt[k][l] == i:
                    num_i += 1
                if ttt[k][l] == j:
                    num_j += 1

            if num_i + num_j == 3 and num_i >= 1 and num_j >= 1:
                win = True
        
        # 세로로 한 줄을 맞췄을 때
        for k in range(MAX_A):
            num_i, num_j = 0, 0
            for l in range(MAX_A):
                if ttt[l][k] == i:
                    num_i += 1
                
                if ttt[l][k] == j:
                    num_j += 1
            
            if num_i + num_j == 3 and num_i >= 1 and num_j >= 1:
                win = True
        
        # 대각선 왼쪽 위에서 오른쪽 아래로
        num_i, num_j = 0, 0
        for k in range(MAX_A):
            if ttt[k][k] == i:
                num_i += 1
            if ttt[k][k] == j:
                num_j += 1
        if num_i + num_j == 3 and num_i >= 1 and num_j >= 1:
                win = True
        
        # 대각선 왼쪽 위에서 오른쪽 아래로
        num_i, num_j = 0, 0
        for k in range(MAX_A):
            if ttt[k][MAX_A - k - 1] == i:
                num_i += 1
            if ttt[k][MAX_A - k - 1] == j:
                num_j += 1
        if num_i + num_j == 3 and num_i >= 1 and num_j >= 1:
            win = True
    
        if win:
            ans += 1

print(ans)