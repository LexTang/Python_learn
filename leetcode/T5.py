class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        a, b = 0, 0
        dp = [[False] * n for _ in range(n)]
        for j in range(1, n):
            for i in range(j):
                if j - i < 3:
                    dp[i][j] = True if s[i] == s[j] else False
                else:
                    dp[i][j] = True if s[i] == s[j] and dp[i + 1][j - 1] else False
                if j - i > b - a and dp[i][j]:
                    a, b = i, j
        return s[a:b + 1]


s = Solution()
print(s.longestPalindrome("bb"))
