n = int(input())
states1 = []
states = {}
for i in range(n):
    state = ""
    for j in range(8):
        state += input()
    states1.append(state)
    if state not in states:
        states[state] = 1
    else:
        states[state] += 1
time = []
for i in range(n-1, -1, -1):
    time.append(states[states1[i]])
    states[states1[i]] -= 1
time = time[::-1]
for t in time:
    print(t)
