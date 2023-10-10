class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        nums.sort()
        for i in range(len(nums)):
            if k == 0:
                break
            if nums[i] < 0:
                nums[i] *= -1
                k -= 1
            elif k % 2 > 0:
                nums[nums.index(min(nums))] *= -1
                break
            else:
                break
        if k%2 > 0:
            nums[nums.index(min(nums))] *= -1
        return sum(nums)
