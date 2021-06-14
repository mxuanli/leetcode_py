class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        """
        问题可以看作是背包容量为 ⌊sum/2⌋，物品重量和价值均为stones[i]的 0-1 背包问题。
        定义二维布尔数组dp，其中 dp[i+1][j] 表示前 i 个石头能否凑出重量 j。
        边界条件去前0个石头一定能凑出重量0，dp[0][0] = True
        当j < stones[i]，则不能凑出重量 j，dp[i][j] = dp[i - 1][j]。
        当 j >= stones[i]，则 dp[i][j] = dp[i - 1][j] or dp[i - 1][j - stones[i]]。
        """
        stones_sum = sum(stones)
        n = len(stones)
        m = stones_sum // 2
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            stone = stones[i - 1]
            for j in range(m + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= stone:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - stone]
        r = None
        for j in range(m, -1, -1):
            if dp[n][j]:
                r = stones_sum - 2 * j
                break
        return r
