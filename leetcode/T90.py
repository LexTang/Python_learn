class Solution:
    def subsetsWithDup(self, nums: list[int]):
        nums.sort()
        result = set()
        self.seg(nums, 0, [], result)
        return list(result)

    def seg(self, nums, idx, tmp, result):
        result.add(tuple(tmp[:]))
        # 终止条件
        if idx == len(nums):
            return
        # 循环递归
        for i in range(idx, len(nums)):
            tmp.append(nums[i])
            self.seg(nums, i + 1, tmp, result)
            tmp.pop()


s = Solution()
print(s.subsetsWithDup([2,3,1,2]))
