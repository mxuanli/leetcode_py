class Solution:
    def maxProfit1(self, prices: list) -> int:
        if not prices and len(prices) == 1:
            return 0
        if len(prices) == 2:
            if prices[1] > prices[0]:
                return prices[1] - prices[0]
            else:
                return 0
        n = len(prices)
        index_ = 0  # 第几天
        status_ = 0  # 0为不持有，1为持有
        count_ = 0  # 交易次数
        d = dict()

        def foo(index, status, count):
            if (index, status, count) in d.keys():
                return d[(index, status, count)]
            if index == n or count == 2:
                return 0
            a, b, c = 0, 0, 0
            # 不操作
            a = foo(index + 1, status, count)
            if status:
                # 持有后卖出
                b = foo(index + 1, 0, count + 1) + prices[index]
            else:
                # 不持有但买入
                c = foo(index + 1, 1, count) - prices[index]
            max_ = max(a, b, c)
            d[(index, status, count)] = max_
            return max_

        r = foo(index_, status_, count_)
        return r

    def maxProfit(self, prices: list) -> int:
        # 官方解
        buy1, buy2 = -prices[0], -prices[0]
        sell1, sell2 = 0, 0
        for i in range(1, len(prices)):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])
        return sell2

    def run(self):
        prices = [7, 6, 4, 3, 1]
        r = self.maxProfit(prices)
        print(r)


s = Solution()
s.run()
