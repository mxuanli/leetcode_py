class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")


class Solution1:
    def hammingWeight(self, n: int) -> int:
        r = 0
        for i in range(32):
            # n 和 2 的 n 次方 做与运算，只有 n 的第 i 位时，运算结果才不为0
            if n & (1 << i):
                r += 1
        return r
