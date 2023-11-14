N = int(input())

hills = [int(input()) for _ in range(N)]


cost = 0

highest = max(hills)
lowest = min(hills)
diff = highest - lowest
cost = 0
while highest - lowest > 17:
    highest -= 1
    lowest += 1
diff2 = highest - lowest

print(abs(diff2 - diff) * 3)