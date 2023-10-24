class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        prev1 = 1
        prev2 = 2

        for i in range(3, n + 1):
            total = prev1 + prev2
            prev1 = prev2
            prev2 = total

        return prev2
