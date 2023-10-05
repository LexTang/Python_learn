# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
# 有效的 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
class Solution:
    def restoreIpAddresses(self, s: str):
        result = []
        self.seg(s, 0, [], result)
        return result

    def seg(self, s, idx, tmp, result):
        if len(tmp) == 4 and idx == len(s):
            result.append('.'.join(tmp))
            return
        for i in range(idx, min(idx + 3, len(s))):
            if self.valid(idx, i + 1, s):
                tmp.append(s[idx:i + 1])
                self.seg(s, i + 1, tmp, result)
                tmp.pop()

    def valid(self, start, end, s):
        if end - start > 1:
            if s[start] != '0':
                return 0 <= int(s[start:end]) <= 255
            else:
                return False
        return 0 <= int(s[start:end]) <= 255


s = Solution()
print(s.restoreIpAddresses("00001"))
