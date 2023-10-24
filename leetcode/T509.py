class Solution:
    cache = {0: 0, 1: 1}
    def fib(self, n: int) -> int:
        if n in Solution.cache:
            return Solution.cache[n]
        val = self.fib(n-1)+self.fib(n-2)
        Solution.cache[n] = val
        return val