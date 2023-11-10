class Solution:
    def rob(self, nums: list[int]) -> int:
        # n = len(nums)
        # dp = [0] * n
        # dp[0] = nums[0]
        # for i in range(1, n):
        #     if i == 1:
        #         dp[i] = max(dp[i-1], nums[i])
        #         continue
        #     dp[i] = max(dp[i-1], nums[i]+dp[i-2])
        # return dp[n-1]
        if len(nums) == 1:
            return nums[0]
        cur, pre = nums[0], 0
        for num in nums[1:]:
            cur, pre = max(pre + num, cur), cur
        return max(cur, pre)
