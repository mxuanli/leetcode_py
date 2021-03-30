class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        d1 = defaultdict(int)
        for i in s:
            d1[i] += 1
        tmp = 0
        for v in d1.values():
            if v % 2 != 0:
                tmp += 1
                if tmp > 1:
                    return False
        return True
