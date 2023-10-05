class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        old = True
        new = True
        length = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            new = (nums[i] - nums[i-1] > 0)
            if length == 1 and nums[i] != nums[i - 1]:
                length += 1
                old = new
            elif new != old:
                length += 1
                old = new
        return length


s = Solution()
print(s.wiggleMaxLength([0, 0]))
