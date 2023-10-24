def multi(A, B):
    # 创建一个结果矩阵C，初始化为零
    C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    # 逐行遍历第一个矩阵
    for i in range(len(A)):
        # 逐列遍历第二个矩阵
        for j in range(len(B[0])):
            # 对应元素相乘并累加
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
    return C


n, d = map(int, input().split())
Q, K, V = [], [], []
for i in range(n):
    Q.append(list(map(int, input().split())))
for i in range(n):
    K.append(list(map(int, input().split())))
for i in range(n):
    V.append(list(map(int, input().split())))
W = list(map(int, input().split()))
# 转置K
KT = [[0] * n for _ in range(d)]
for i in range(d):
    for j in range(n):
        KT[i][j] = K[j][i]
# Q乘KT
Q_KT = multi(Q, KT)
Q_KT_V = multi(Q_KT, V)
for i in range(len(W)):
    for j in range(len(Q_KT_V[i])):
        Q_KT_V[i][j] *= W[i]
for data in Q_KT_V:
    print(' '.join(map(str, data)))
