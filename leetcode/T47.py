class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        self.seg(result, nums, [0 for _ in range(len(nums))], [])
        return result

    def seg(self, result, nums, used, tmp: list[int]):
        # 终止条件
        if len(tmp) == len(nums):
            result.append(tmp[:])
            return
        # 循环递归
        for i in range(len(nums)):
            # 判断是否被使用
            if (i > 0 and nums[i] == nums[i - 1] and used[i - 1] == 1) or used[i] == 1:
                continue
            used[i] += 1
            tmp.append(nums[i])
            self.seg(result, nums, used, tmp)
            tmp.pop()
            used[i] -= 1


s = Solution()
print(s.permuteUnique([1, 3, 1]))
