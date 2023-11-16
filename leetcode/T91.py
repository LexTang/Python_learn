class Solution:
    def numDecodings(self, s: str) -> int:
        lens = len(s) + 1
        if lens == 1:
            return 0
        dp0, dp1, dp2 = 0, 1, 0
        for i in range(1, lens):
            dp2 = 0
            if s[i - 1] != '0':
                dp2 += dp1
            if i > 1 and s[i - 2] != '0' and int(s[i - 2:i]) <= 26:
                dp2 += dp0
            dp0, dp1 = dp1, dp2
        return dp2


s = Solution()
print(s.numDecodings("12303"))
