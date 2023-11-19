n, a, b = map(int, input().split())
fields = [[]] * n
for i in range(n):
    fields[i] = list(map(int, input().split()))
area = 0
for field in fields:
    x1, y1, x2, y2 = field
    if x1 >= a or y1>= b or x2 <= 0 or y2 <= 0:
        continue
    area += (min(a, x2) - max(0, x1)) * (min(b, y2) - max(0, y1))
print(area)
