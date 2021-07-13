class Solution:
    def reverseBits(self, n: int) -> int:
        r = 0
        for i in range(32):
            r = (r << 1) | (n & 1)
            n >>= 1
        return r


class Solution1:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res <<= 1  # 新增一位
            res += n & 1  # 取出来最后一位，并加到res
            n >>= 1  # 去除最后一位
        return res
