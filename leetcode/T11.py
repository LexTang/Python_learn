class Solution:
    def maxArea(self, height: list[int]) -> int:
        a, b = 0, len(height)-1
        area = 0
        while a < b:
            area = max((b-a)*min(height[a], height[b]), area)
            if height[a] > height[b]:
                b -= 1
            else:
                a += 1
        return area