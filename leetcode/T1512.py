class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        hash = [0] * 101
        ans = 0
        for num in nums:
            ans += hash[num]
            hash[num] += 1
        return ans
