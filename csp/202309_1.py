n, m = map(int, input().split())
alt, loc = [], []
for i in range(n):
    alt.append(list(map(int, input().split())))
for i in range(m):
    loc.append(list(map(int, input().split())))
for i in range(m):
    for j in range(n):
        loc[i][0] += alt[j][0]
        loc[i][1] += alt[j][1]
for key in loc:
    print(key[0], key[1])
