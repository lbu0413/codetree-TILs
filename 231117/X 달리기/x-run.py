import sys

min_ = sys.maxsize
X = int(input())

for i in range(X):
    distance, speed, time = 0, 0, 0
    while True:

        if distance == X and speed == 1:
            break

        if (X - distance) < distance:
            speed -= 1
        
        elif (X - distance) == distance:
            speed -= 0
        
        else:
            speed += 1
        
        distance += speed
        time += 1
    
    min_ = min(min_, time)

print(min_)