class Solution:
    def numWays(self, n: int) -> int:
        # 和70题一样
        if n <= 1:
            return 1
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n] % (10 ** 9 + 7)
