class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
        # hash = [0] * 123
        # for s in sentence:
        #     hash[ord(s)] += 1
        # for i in range(97, 123):
        #     if hash[i] == 0:
        #         return False
        # return True
