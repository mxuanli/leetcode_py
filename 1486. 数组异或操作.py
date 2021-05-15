class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        r = start + 2 * 0
        for i in range(1, n):
            num = start + 2 * i
            r ^= num
        return r


class Solution1:
    def xorOperation(self, n: int, start: int) -> int:
        r = 0
        for i in range(n):
            num = start + 2 * i
            r ^= num
        return r
