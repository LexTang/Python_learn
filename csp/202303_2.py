n, m, k = map(int, input().split())
size, lis = 0, [[]] * n
for i in range(n):
    t, c = map(int, input().split())
    lis[i] = [t, c]
    size = max(t, size)
tc = [0] * (size + 1)
for t, c in lis:
    tc[t] += c
i = size
while i > k:
    c = tc[i]
    if m < c:
        break
    m -= c
    i -= 1
    tc[i] += c
print(i)
