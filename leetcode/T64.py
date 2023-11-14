class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        x, y = len(grid[0]), len(grid)
        for i in range(1, x):
            grid[0][i] += grid[0][i-1]
        for i in range(1, y):
            grid[i][0] += grid[i-1][0]
        for i in range(1, y):
            for j in range(1, x):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]


s = Solution()
print(s.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
