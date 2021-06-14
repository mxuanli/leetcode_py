class Solution:
    def numSquares(self, n: int) -> int:
        """
        dp[i]表示和为i的完全平方数的最小数量
        边界条件dp[0] = 0
        转移方案
        遍历 1 - n 记为 i，然后遍历 1 - √￣i 的完全平方数 记为 j，求 i - j * j 的最小方案数，最后加上外层循环 i 的一个数字，总量 + 1。
        dp[i] = min([i - j * j]) + 1
        """
        INF = 10 ** 9 + 7
        dp = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            minn = INF
            j = 1
            while j * j <= i:
                minn = min(minn, dp[i - j * j])
                j += 1
            dp[i] = minn + 1
        return dp[n]
