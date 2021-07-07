class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        dp = [0 for _ in range(n + 1)]  # dp[i]表示爬到第i个台阶的时候方法数
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]  # 状态转移公式
        return dp[n]
