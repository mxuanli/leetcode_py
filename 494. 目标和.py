class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        记数组的元素和为 sum，添加 - 号的元素之和为 neg，则其余添加 + 的元素之和为 sum−neg，得到的表达式的结果为
        (sum − neg) − neg = sum − 2 * neg = target
        neg = sum - target // 2
        如果sum - target为奇数，则代表没有方案，返回0
        选取若干元素等于neg，方案数和不同表达式结果为target是一样的
        """
        nums_sum = sum(nums)
        if target > nums_sum:
            return 0
        diff = nums_sum - target
        if diff % 2 != 0:
            return 0
        neg = diff // 2
        # dp[i][j]前i个元素，和为neg的方案数
        # 边界条件，dp[0][j] = 0 if j = 0，dp[0][0] = 1
        # 遍历 1 <= i <= n，1 <= i <= neg
        # 选择，如果j < num 则dp[i][j] = dp[i - 1][j]，如果j > num，则dp[i][j] = dp[i - 1][j] + dp[i-1][j-num]
        n = len(nums)
        dp = [[0] * (neg + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            num = nums[i - 1]
            for j in range(neg + 1):
                dp[i][j] = dp[i - 1][j]  # 继承
                # 选择
                if j >= num:
                    dp[i][j] += dp[i - 1][j - num]
        return dp[n][neg]


class Solution1:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        记数组的元素和为 sum，添加 - 号的元素之和为 neg，则其余添加 + 的元素之和为 sum−neg，得到的表达式的结果为
        (sum − neg) − neg = sum − 2 * neg = target
        neg = sum - target // 2
        如果sum - target
        """
        nums_sum = sum(nums)
        if target > nums_sum:
            return 0
        diff = nums_sum - target
        if diff % 2 != 0:
            return 0
        neg = diff // 2
        n = len(nums)
        dp = [0 for _ in range(neg + 1)]

        dp[0] = 1
        for i in range(1, n + 1):
            num = nums[i - 1]
            for j in range(neg, num - 1, -1):
                dp[j] += dp[j - num]
        return dp[neg]
