class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        dp = [0 for _ in range(n)]  # dp[i]表示在第i天的最大利润，边界条件是dp[0] = 0
        min_price = prices[0]
        for i in range(1, n):
            price = prices[i]  # 今天价格
            min_price = min(min_price, price)
            dp[i] = max(dp[i - 1], price - min_price)  # 状态转移
        return dp[-1]


class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        r = 0
        min_price = float('inf')  # float('inf')表示负无穷
        for price in prices:
            min_price = min(min_price, price)  # 截止到当前的最低价（买入价）
            r = max(r, price - min_price)  # 截止到目前的最高利润
        return r
