from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, begin, path, res, target):
            if target == 0:
                res.append(path[:])
                return
            for i in range(begin, len(candidates)):
                if candidates[i] > target:
                    continue
                path.append(candidates[i])
                dfs(candidates, i, path, res, target - candidates[i])
                path.pop()

        candidates.sort()
        res = []
        dfs(candidates, 0, [], res, target)
        return res


s = Solution()
print(s.combinationSum(candidates=[2, 3, 6, 7], target=7))
