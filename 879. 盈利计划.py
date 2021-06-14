class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        """
        p[i][j][k] 表示在前 i 个工作中选择了 j 个员工，并且满足工作利润至少为 k 的情况下的盈利计划的总数目
        p[length][n][minProfit]
        边界p[0][0][0] = 1
        状态转移公式
        if j < group[i]：dp[i][j][k] = dp[i - 1][j][k]
        if j >= group[i]：dp[i][j][k] = dp[i - 1][j][k] + d[i - 1][group[i] - j][max(0, k - profit[i])]
        """
        MOD = 10 ** 9 + 7
        length = len(group)  # 小组数 & 工作数
        dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(length + 1)]
        dp[0][0][0] = 1
        for i in range(1, length + 1):
            g = group[i - 1]
            p = profit[i - 1]
            for j in range(n + 1):
                for k in range(minProfit + 1):
                    dp[i][j][k] = dp[i - 1][j][k]
                    if j >= g:
                        dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j - g][max(0, k - p)]) % MOD
        r = sum(dp[length][j][minProfit] for j in range(n + 1))
        return r % MOD
