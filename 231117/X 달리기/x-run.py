# 현재 이 속도를 올렸을때/유지했을 때 문제 조건을 만족하며 도착지에 도달하는 것이 가능한지에 대해 고민해보면 식을 발견
# 이를 기준으로 속도를 더 올릴지/유지할지/감소해야할지에 대한 판단을 해볼 수 있습니다 :)
import sys

min_ = sys.maxsize
X = int(input())

for i in range(1, X + 1):
    distance, speed, time = 0, 0, 0
    while True:
        if distance == X: # 목적지에 도착하면 종료
            break

        if distance >= i: # 속도를 줄여야하는 지점에 진입
            if speed == 1:
                speed = 1
            else:
                speed -= 1
        else:
            speed += 1

        
        distance += speed
        time += 1

    if speed != 1:
        continue
    else:
        min_ = min(min_, time)

print(min_)