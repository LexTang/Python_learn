class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        if n <= 0:
            return []
        res = []
        self.gen(res, "", n, n)
        return res

    def gen(self, res, str, left, right):
        if left == 0 and right == 0:
            res.append(str)
            return
        if left == right:
            self.gen(res, str + "(", left - 1, right)
        elif left < right:
            if left > 0:
                self.gen(res, str + "(", left - 1, right)
            self.gen(res, str + ")", left, right - 1)

