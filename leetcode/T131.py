# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
# 返回 s 所有可能的分割方案。
# 示例: 输入: "aab" 输出: [ ["aa","b"], ["a","a","b"] ]
class Solution:

    def partition(self, s: str):
        # 用于存储最终的回文子串组合
        result = []
        # 调用递归函数，start_index 初始为 0，path 用于记录当前组合，result 用于存储结果
        self.backtracking(s, 0, [], result)
        return result

    def backtracking(self, s, start_index, path, result):
        # 基本情况：如果 start_index 到达字符串的末尾，表示找到一种回文子串组合
        if start_index == len(s):
            result.append(path[:])  # 将当前回文子串组合添加到结果中
            return

        # 单层递归逻辑：从 start_index 开始尝试切割字符串
        for i in range(start_index, len(s)):
            # 此处多了一步判断：检查被截取的子串 [start_index, i] 是否为回文串
            if self.is_palindrome(s, start_index, i):
                path.append(s[start_index:i + 1])  # 将回文子串添加到当前组合
                self.backtracking(s, i + 1, path, result)  # 递归：继续从下一处开始切割，判断其余是否仍为回文串
                path.pop()  # 回溯：将最后一个添加的子串弹出，尝试其他组合

    def is_palindrome(self, s: str, start: int, end: int) -> bool:
        i: int = start
        j: int = end
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


