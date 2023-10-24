class Solution:
    def candy(self, ratings: list[int]) -> int:
        size = len(ratings)
        kid = [1 for _ in range(size)]
        for i in range(1, size):
            if ratings[i] > ratings[i-1]:
                kid[i] = kid[i-1] + 1
        for i in range(size-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                kid[i] = max(kid[i+1] + 1, kid[i])
        return sum(kid)


s = Solution()
print(s.candy([1,2,87,87,87,2,1]))
