class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        x, y = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(y)] for _ in range(x)]
        area = 0
        for i in range(0, y):
            dp[0][i] = 1 if matrix[0][i] == '1' else 0
            area = max(dp[0][i], area)
        for i in range(1, x):
            dp[i][0] = 1 if matrix[i][0] == '1' else 0
            area = max(dp[i][0], area)
        for i in range(1, x):
            for j in range(1, y):
                if matrix[i][j] == '0':
                    continue
                dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                area = max(dp[i][j], area)
        return area ** 2

s = Solution()
print(s.maximalSquare(
    [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
