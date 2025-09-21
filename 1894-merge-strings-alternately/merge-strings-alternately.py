class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)

        ret = ''
        i1 = 0
        i2 = 0
        prev_word1 = False

        while i1 < n1 or i2 < n2:
            if not prev_word1 and i1 < n1:
                ret += word1[i1]
                i1 += 1
                prev_word1 = True
            elif prev_word1 and i2 < n2:
                ret += word2[i2]
                i2 += 1
                prev_word1 = False
            elif i1 < n1:
                ret += word1[i1]
                i1 += 1
                prev_word1 = True
            elif i2 < n2:
                ret += word2[i2]
                i2 += 1
                prev_word1 = False

        return ret

