class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        完全背包
        dp[i] 表示总金额为i时候的方案数
        边界条件：dp[0] = 1，总金额为0的时候，方案只有一个，就是什么都不选
        转移方案
        遍历coins，然后遍历从coin到amount，记为i，
        然后，dp[i] = dp[i] + dp[i - coin]
        dp[i]的方案数，等于能组合成dp[i]的方案数，加上dp[i - coin]的方案数（因为外层循环有一个coin，i - coin + coin）
        """
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = dp[i] + dp[i - coin]
        return dp[amount]
