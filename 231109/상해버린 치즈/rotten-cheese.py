class Info1:
    def __init__(self, p, m, t): # p 사람 , m 치즈, t, 먹은 시간
        self.p, self.m, self.t = p, m , t
    

class Info2 :
    def __init__(self, p, t): # p 사람, t 아픈 시간
        self.p, self.t = p, t


n, m, d, s = map(int, input().split()) # n 사람의 수, m 치즈의 수, d 치즈를 먹은 기록의 수, s 아픈 기록의 수

info1 = []
for i in range(d):
    p, x, t = map(int, input().split())
    info1.append(Info1(p, x, t))

info2 = []
for i in range(s):
    p, t = map(int, input().split())
    info2.append(Info2(p, t))


ans = 0
for i in range(1, m+1): 
    
    time = [0] * (n + 1)

    for info in info1:
        if info.m != i:
            continue
        person = info.p
        if time[person] == 0:
            time[person] = info.t
        
        if time[person] > info.t:
            time[person] = info.t

    possible = True # i번째 치즈가 상했을 수 있으면 true 아니면 false

    for info in info2:
        person = info.p
        if time[person] == 0: # 만약 아픈 기록이 없다면 모순.
            possible = False
        
        if time[person] >= info.t: # 만약 아픈 기록이 치즈 먹은 기록 보다 빠르다면 모순
            possible = False
    
    pill = 0
    if possible:
        for j in range(1, n+1):
            if time[j] > 0:
                pill += 1

    ans = max(ans, pill)

print(ans)