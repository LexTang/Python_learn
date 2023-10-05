# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
# 每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        result = []
        self.seg(n, result, [], ['.' for _ in range(n)])
        return result

    def seg(self, n, result, tmp, sta):
        if len(tmp) == n:
            result.append(tmp[:])
            return
        for i in range(n):
            if len(tmp) > 0 and self.check(tmp, i, len(tmp)):
                continue
            sta[i] = "Q"
            tmp.append(''.join(sta[:]))
            sta = ['.' for _ in range(n)]
            self.seg(n, result, tmp, sta)
            tmp.pop()
            sta = ['.' for _ in range(n)]

    def check(self, tmp, x, y):
        # 检查上方
        j = y-1
        while j >= 0:
            if tmp[j][x] == 'Q':
                return True
            j -= 1
        # 检查右上方
        i, j = x-1, y-1
        while i >= 0 and j >= 0:
            if tmp[j][i] == "Q":
                return True
            i -= 1
            j -= 1
        # 检查左上方
        i, j = x+1, y-1
        while i < len(tmp[0]) and j >= 0:
            if tmp[j][i] == "Q":
                return True
            i += 1
            j -= 1


s = Solution()
print(s.solveNQueens(4))
