class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        # dp[i]表示在i时候的最大金额
        dp = [0] * n
        # 边界条件，第一房屋时候为本身，第二个房屋时候为前两个的最大值
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            # 状态转移，当前的最大值要么等于上一个的最大值，要么等于当前值加上上一个的值
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        return max(dp)


class Solution1:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        a, b = 0, 0  # a存上上一个，b存上一个
        for i in range(n):
            a, b = b, max(b, a + nums[i])
        return b
