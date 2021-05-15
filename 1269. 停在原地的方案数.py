
class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        ######
        # 1. 创建dp数组，dp[i][j]表示操作了i次之后，下标位于j的方案数
        # dp[steps + 1][arrLen + 1]
        # 因为dp[0][0]存的是没有操作且位于i的值，所以i的取值是1 - steps + 1，j的是1 - arrLen + 1
        ######
        mod = 10 ** 9 + 7  # 方案数要模 10^9 + 7
        max_col = min(steps, arrLen - 1)  # 一共操作steps步，所以j一定小于steps和arrLen
        dp = [[0] * (max_col + 1) for _ in range(steps + 1)]
        # 设置边界条件
        dp[0][0] = 1
        ######
        # dp
        # 状态转移方程 dp[i][j]=dp[i−1][j−1]+dp[i−1][j]+dp[i−1][j+1]
        ######
        for i in range(1, steps + 1):
            for j in range(0, max_col + 1):
                dp[i][j] = dp[i - 1][j]
                if j > 0:  # 防止越界
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % mod
                if j < max_col:  # 防止越界
                    dp[i][j] = (dp[i][j] + dp[i - 1][j + 1]) % mod
        return dp[steps][0]


class Solution2:

    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10 ** 9 + 7  # 方案数要模 10^9 + 7
        max_col = min(steps, arrLen - 1)  # 一共操作steps步，所以j一定小于steps和arrLen
        dp = [0] * (steps + 1)
        # 设置边界条件
        dp[0] = 1
        # dp
        # 状态转移方程 dp[i][j]=dp[i−1][j−1]+dp[i−1][j]+dp[i−1][j+1]
        for i in range(1, steps + 1):
            dp_next = [0] * (steps + 1)
            for j in range(0, max_col + 1):
                dp_next[j] = dp[j]
                if j > 0:  # 防止越界
                    dp_next[j] = (dp_next[j] + dp[j - 1]) % mod
                if j < max_col:  # 防止越界
                    dp_next[j] = (dp_next[j] + dp[j + 1]) % mod
            dp = dp_next
        return dp[0]
