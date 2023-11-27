from typing import List

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        # lamt = len(mat)
        k %= len(mat[0])
        for ma in mat:
            if ma[k:]+ma[:k] != ma:
                return False
        return True
