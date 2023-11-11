N = int(input())
MAX = 10 + 1

points = [tuple(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(MAX):
    for j in range(MAX):
        for k in range(MAX):

            success = True

            for x, y in points: # 가로 직선 3개로 커버가 되는지 확인
                if x == i or x == j or x == k:
                    continue

                else:
                    success = False
            if success:
                ans = 1
            
            success = True
            for x, y in points: #가로 직선 2개 세로 선 1개로 커버 가능한지 확인
                if x == i or x == j or y == k:
                    continue
                
                else:
                    success = False
            
            if success:
                ans = 1
            

            success = True
            for x, y in points: # 가로1 세로2
                if y == i or x == j or y == k:
                    continue
                
                else:
                    success = False
            
            if success:
                ans = 1
            
            success = True
            for x, y in points:
                if y == i or y == j or y == k:
                    continue
                else:
                    success = False
            
            if success:
                ans = 1

print(ans)