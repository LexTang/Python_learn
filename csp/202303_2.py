n, m, k = map(int, input().split())
size, dic = 0, {}
for i in range(n):
    t, c = map(int, input().split())
    if t in dic:
        dic[t] += c
    else:
        dic[t] = c
    size = max(t, size)
tc = [0] * (size + 1)
for t, c in dic.items():
    tc[t] = c
i = size
while i > k:
    c = tc[i]
    if m < c:
        break
    m -= c
    i -= 1
    tc[i] += c
print(i)
