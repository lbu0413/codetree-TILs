import sys

min_ = sys.maxsize
X = int(input())

for i in range(X):
    distance, speed, time = 0, 0, 0
    while True:
        if distance == X and speed == 1: # 목적지에 도착하면 종료
            break

        if speed + distance > (X // 2): # 속도를 줄여야하는 지점에 진입
            if speed == 1:
                speed = 1
            else:
                speed -= 1
        else:
            speed += 1
        
        distance += speed
        time += 1
    
    min_ = min(min_, time)

print(min_)