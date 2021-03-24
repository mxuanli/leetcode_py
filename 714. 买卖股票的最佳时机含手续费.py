class Solution:

    def maxProfit(self, prices: list, fee: int) -> int:
        buy = sell = prices[0]
        r = 0
        for p in prices:
            if buy < sell - fee:  # 如果卖出价格-首付费大于买入价格，说明当前是可以赚的
                if p < sell - fee:  # 如果当天价格小于卖出价格-手续费，就把股票卖出再重新买入
                    r += sell - fee - buy
                    buy = sell = p
                elif p > sell:  # 当天价格大于上一个卖出价格，则修改卖出价格
                    sell = p
            else:
                sell = p if p > sell else sell  # 当天价格大于上一个卖出价格，则修改卖出价格
                if p < buy:  # 当日价格小于买入价格，则修改为当日买入
                    buy = sell = p
        if buy < sell - fee:
            r += sell - fee - buy
        return r

    def maxProfit2(self, prices: list, fee: int) -> int:
        r0 = 0  # 不持有时候的最大利润
        r1 = -prices[0]  # 持有时候的最大利润（0-买入的费用）
        for i in prices:
            r0 = max(r0, r1 + i - fee)  # 前一天不持有和前一天持有今天卖出的最大值
            r1 = max(r1, r0 - i)  # 前一天持有和前一天不持有但今天买入的最大值
        return r0

    def run(self):
        prices = [1, 3, 2, 8, 4, 9]
        fee = 2
        r = self.maxProfit2(prices, fee)
        print(r)


s = Solution()
s.run()
