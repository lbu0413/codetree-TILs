X = int(input())


distance, time, speed = 0, 0, 1

distance_left = X 

while True:
    if distance_left == 0:
        break
    
    distance_left -= speed
    time += 1

    if distance_left >= (speed + 1) * (speed + 2) // 2:
        speed += 1

    elif distance_left >= (speed) * (speed + 1) // 2:
        pass
    
    else:
        speed -= 1

print(time)