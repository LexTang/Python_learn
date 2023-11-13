class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        size = len(triangle)
        dp = [[]] * size
        for i in range(size):
            dp[i] = [0] * (i + 1)
        dp[0][0] = triangle[0][0]
        for i in range(1, size):
            dp[i][0] = dp[i - 1][0] + triangle[i][0]
            dp[i][-1] = dp[i - 1][-1] + triangle[i][-1]
            for j in range(1, i):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
        return min(dp[-1])
