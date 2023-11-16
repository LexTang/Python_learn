class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        lens = len(s) + 1
        dp = [False] * lens
        dp[0] = True
        for i in range(1, lens):
            for j in range(i):
                if dp[j] and (s[j:i] in wordDict):
                    dp[i] = True
                    break
        return dp[-1]


s = Solution()
print(s.wordBreak("aaaaaaa", ["aaaa", "aaa"]))
