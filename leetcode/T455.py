class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        index = 0
        for i in range(len(s)):
            if index < len(g) and g[index] <= s[i]:
                index += 1
        return index
