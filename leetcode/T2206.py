from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hash = []*501
        for num in nums:
            hash[num] += 1
        for i in range(501):
            if hash[i] % 2 == 1:
                return False
        return True
