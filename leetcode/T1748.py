from typing import List

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        hash = [0] * 101
        for num in nums:
            hash[num] += 1
        sum0 = 0
        for i in range(101):
            sum0 += i if hash[i] == 1 else 0
        return sum0


