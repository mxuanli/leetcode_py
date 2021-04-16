class Solution:

    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) == 0:
            return True
        if len(s1) == 1:
            if s1 == s2:
                return True
            return False
        if sorted(s1) != sorted(s2):
            return False
        for i in range(1, len(s1)):
            if self.isScramble(s1[i:], s2[i:]) and self.isScramble(s1[:i], s2[:i]):
                return True
            elif self.isScramble(s1[i:], s2[:len(s2) - i]) and self.isScramble(s1[:i], s2[len(s2) - i:]):
                return True
        return False


s1 = "abcde"
s2 = "caebd"
s = Solution()
r = s.isScramble(s1, s2)
print(r)
