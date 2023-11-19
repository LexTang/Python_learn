n, m, k = map(int, input().split())
tc = {}
for i in range(n):
    t, c = map(int, input().split())
    if t in tc:
        tc[t] += c
    else:
        tc[t] = c
tc = [[key, value] for key, value in tc.items()]
tc = sorted(tc, key=lambda x: x[0], reverse=True)
i, end = 0, len(tc) - 1
day = 0
while i <= end:
    t, c = tc[i]
    if t <= k or m < c:
        day = k if t <= k else t
        break
    if i == end:
        day = max(k, day - (m // c))
        break
    if m > (t - tc[i + 1][0]) * c:
        m -= (t - tc[i + 1][0]) * c
        tc[i + 1][1] += c
        i += 1
        continue
    tc[i][0] -= 1
    m -= c
print(day)
