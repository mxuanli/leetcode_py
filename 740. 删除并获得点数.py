class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """
        total计算nums内某个数字的总和，如果删除了某个数字，那么它相邻的两个数字也会被删除，所以可以获得这个数字的所有点数。
        total是从 0 到 元素的最大值，所以 i 和 i - 2 肯定是不相邻的，就可以使用198. 打家劫舍的dp解法。
        """
        max_num = max(nums)
        total = [0 for _ in range(max_num + 1)]
        for num in nums:
            total[num] += num

        def foo(total: List[int]):
            a, b = total[0], max(total[0], total[1])
            for i in range(2, max_num + 1):
                a, b = b, max(b, a + total[i])
            return b

        return foo(total)
