class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        r = 0
        n = len(nums)
        for i in range(30):
            # (num >> i) & 1 去除第 i 位的值
            c = sum([(num >> i) & 1 for num in nums])
            r += c * (n - c)  # c * (n - c) 计算某一位的汉明距离
        return r
