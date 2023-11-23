class Solution:
    def myAtoi(self, s: str) -> int:
        i, n = 0, len(s)

        # 移除前导空格
        while i < n and s[i] == ' ':
            i += 1

        # 处理正负号
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # 逐字符解析数字
        result = 0
        while i < n and '0' <= s[i] <= '9':
            digit = int(s[i])

            # 检查溢出
            if result > (2 ** 31 - 1) // 10 or (result == (2 ** 31 - 1) // 10 and digit > 7):
                return 2 ** 31 - 1 if sign == 1 else -2 ** 31

            result = result * 10 + digit
            i += 1

        return sign * result
 