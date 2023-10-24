class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        cur = 0
        start = 0
        for i in range(len(gas)):
            cur += gas[i] - cost[i]
            if cur < 0:
                start = i + 1
                cur = 0
        return start


s = Solution()
print(s.canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))

