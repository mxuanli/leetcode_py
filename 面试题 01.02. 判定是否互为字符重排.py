from collections import defaultdict


class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        return sorted(s1) == sorted(s2)


class Solution2:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for i in range(len(s1)):
            d1[s1[i]] += 1
            d2[s2[i]] += 1
        for k, v in d1.items():
            if d2[k] != v:
                return False
        return True
