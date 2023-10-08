import math

n, m = map(int, input().split())
alt = [None]
for i in range(n):
    a, b = input().split()
    if a == '1':
        alt.append([int(a), float(b)])
    else:
        alt.append([int(a), math.sin(float(b)), math.cos(float(b))])
for i in range(m):
    idx1, idx2, x, y = map(int, input().split())
    for j in range(idx1, idx2+1):
        if alt[j][0] == 1:
            k = alt[j][1]
            x, y = x * k, y * k
        else:
            a, b = alt[j][1], alt[j][2]
            x, y = x * b - y * a, y * b + x * a
    print(f"{x:.3f} {y:.3f}")
