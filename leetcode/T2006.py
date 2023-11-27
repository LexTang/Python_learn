class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        haxi = [0] * 101
        ans = 0
        for num in nums:
            ans += haxi[num + k] if 1 <= num + k <= 100 else 0
            ans += haxi[num - k] if 1 <= num - k <= 100 else 0
            haxi[num] += 1
        return ans
