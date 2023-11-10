class Solution:
    def maximumBags(self, capacity: list[int], rocks: list[int], additionalRocks: int) -> int:
        # sub = []
        mea = len(capacity)
        for i in range(mea):
            rocks[i] = capacity[i] - rocks[i]
        i = 0
        rocks.sort()
        while i < mea and additionalRocks > 0:
            if rocks[i] > additionalRocks:
                break
            additionalRocks -= rocks[i]
            i += 1
        return i


s = Solution()
print(s.maximumBags([2, 3, 4, 5], [1, 2, 4, 4], 2))
