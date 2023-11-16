class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1, len2, len3 = len(s1), len(s2), len(s3)

        # 特判：当 s1 和 s2 的长度之和不等于 s3 的长度时，必然无法交错组成
        if len1 + len2 != len3:
            return False

        # 初始化二维数组 dp
        dp = [[False] * (len2 + 1) for _ in range(len1 + 1)]
        dp[0][0] = True

        # 处理边界情况：s1 为空时的情况
        for j in range(1, len2 + 1):
            dp[0][j] = dp[0][j - 1] and (s2[j - 1] == s3[j - 1])

        # 处理边界情况：s2 为空时的情况
        for i in range(1, len1 + 1):
            dp[i][0] = dp[i - 1][0] and (s1[i - 1] == s3[i - 1])

        # 动态规划的状态转移
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                dp[i][j] = ((dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or
                            (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]))

        # 返回结果
        return dp[len1][len2]

