class Solution:

    def hammingWeight(self, n: int) -> int:
        r = 0
        for i in range(32):
            if n & (1 << i):
                r += 1
        return r
