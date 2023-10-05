# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 说明：解集不能包含重复的子集。
# 示例: 输入: nums = [1,2,3] 输出: [ [3],   [1],   [2],   [1,2,3],   [1,3],   [2,3],   [1,2],   [] ]
class Solution:
    def subsets(self, nums):
        result = []
        self.seg(nums, 0, [], result)
        return result

    def seg(self, nums, idx, tmp, result):
        result.append(tmp[:])
        # 终止条件
        if idx == len(nums):
            return
        # 循环递归
        for i in range(idx, len(nums)):
            tmp.append(nums[i])
            self.seg(nums, i+1, tmp, result)
            tmp.pop()


s = Solution()
nums = [1, 2, 3]
print(s.subsets(nums))
