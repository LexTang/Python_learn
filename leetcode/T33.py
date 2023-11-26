class Solution:
    def search(self, nums: list[int], target: int) -> int:
        a, b = 0, len(nums) - 1
        while a <= b:
            c = (a + b) // 2
            if nums[c] == target:
                return c
            if nums[a] <= nums[c]:
                if nums[a] <= target < nums[c]:
                    b = c - 1
                else:
                    a = c + 1
            else:
                if nums[c] < target <= nums[b]:
                    a = c + 1
                else:
                    b = c - 1
        return -1


s = Solution()
print(s.search(nums=[4,5,6,-1,0,1,2], target=-1))
