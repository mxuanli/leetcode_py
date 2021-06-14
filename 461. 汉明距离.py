class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count("1")


class Solution1:
    def hammingDistance(self, x: int, y: int) -> int:
        nums = x ^ y
        r = 0
        while nums > 0:
            nums &= (nums - 1)
            r += 1
        return r
