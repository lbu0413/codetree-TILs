x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())


x_max = max(x1, x2, x3, x4)
x_min = min(x1, x2, x3, x4)
y_max = max(y1, y2, y3, y4)
y_min = min(y1, y2, y3, y4)

x = x_max - x_min
y = y_max - y_min


area1 = x * x
area2 = y * y
print(max(area1, area2))