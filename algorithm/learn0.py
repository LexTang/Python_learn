import random
import time


# 选择排序
def select(x):
    length = len(x)
    for i in range(length - 1):
        for j in range(i + 1, length):
            if x[j] < x[i]:
                x[i], x[j] = x[j], x[i]
    return x


# 冒泡排序
def bubble(x):
    l = len(x)
    for i in range(l):
        for j in range(1, l - i):
            if x[j] < x[j - 1]:
                x[j], x[j - 1] = x[j - 1], x[j]
    return x


# 插入排序
def insert(x):
    l = len(x)
    for i in range(1, l):
        if x[i] > x[i-1]:
            continue
        for j0 in range(0, i):
            j = i - j0
            if x[j] < x[j-1]:
                x[j], x[j - 1] = x[j - 1], x[j]
    return x


# 归并排序
def sequence(x, f, m, l):
    tmp = []
    a = f
    b = m + 1
    while a <= m and b <= l:
        if x[a] <= x[b]:
            tmp.append(x[a])
            a += 1
        else:
            tmp.append(x[b])
            b += 1
    tmp.extend(x[a:m + 1])
    tmp.extend(x[b:l + 1])
    for i in range(f, l + 1):
        x[i] = tmp[i - f]


def merge(x, f, l):
    if f == l:
        return
    m = (f + l) // 2
    merge(x, f, m)
    merge(x, m + 1, l)
    sequence(x, f, m, l)
    return x


# 桶排序
def bucket(x):
    a = min(x)
    b = max(x)
    count = 3
    buck = [[], [], []]
    perbuck = (b - a + count) // count
    for i in x:
        index = (i - a) // perbuck
        buck[index].append(i)
    for j in range(count):
        select(buck[j])
    temp = 0
    for i in range(count):
        for j in buck[i]:
            x[temp] = j
            temp += 1
    return x


# 计数排序
def counting(x):
    l = len(x)
    tmp = 0
    mid = min(x)
    if mid < 0:
        for i in range(0, l):
            x[i] = x[i] - mid
    al = max(x) + 1
    cal = [0] * al
    for val in x:
        cal[val] += 1
    for val in range(0, al):
        while cal[val] > 0:
            cal[val] -= 1
            x[tmp] = val
            tmp += 1
    if mid < 0:
        for i in range(0, l):
            x[i] = x[i] + mid
    return x


# 基数排序
def radix(x):
    base = 1
    mb = max(x)
    while base < mb:
        holder = [[] for _ in range(19)]  # 创建包含 20 个空列表的列表
        for val in x:
            if val < 0:
                idx = (val // base) % 10
            else:
                idx = (val // base) % 10 + 9
            holder[idx].append(val)
        result = []
        for val in holder:
            result.extend(val)
        x = result
        base *= 10
    return x


# 快速排序
def quick(x):
    a = 0
    b = len(x) - 1
    quicker(x, a, b)
    return x


def quicker(x, a, b):
    if b <= a:
        return
    idx = random.randint(a, b)
    x[a], x[idx] = x[idx], x[a]
    idx = a
    # 保存比基准数小的下标
    s = a + 1
    for i in range(a + 1, b + 1):
        if x[i] < x[idx]:
            x[i], x[s] = x[s], x[i]
            s += 1
    x[s - 1], x[idx] = x[idx], x[s - 1]
    quicker(x, a, s - 1)
    quicker(x, s, b)


# 希尔排序
def xier(x):
    l = len(x)
    step = l // 2
    while step > 0:
        for i in range(0, step):
            p = i
            tmp = []
            while p < l:
                tmp.append(x[p])
                p += step
            tmp = insert(tmp)
            idx = 0
            p = i
            while p < l:
                x[p] = tmp[idx]
                p += step
                idx += 1
        step //= 2
    return x


# 堆排序
def binary(x):
    l = len(x)-1
    for i in range(l, 0, -1):
        heap(x, i)
    return x


def heap(x, a):
    for i in range(a, 0, -1):
        if x[i] > x[(i-1)//2]:
            x[i], x[(i - 1) // 2] = x[(i-1)//2],  x[i]
    x[0], x[a] = x[a], x[0]
    return x


if __name__ == '__main__':
    lis = [10, -9, 8, 7, -6, 5, 0, 4, -3, 2, 1]
    t1 = time.perf_counter()
    print(binary(lis))
    t2 = time.perf_counter()
    print(t2-t1)
