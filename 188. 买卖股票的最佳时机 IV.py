class Solution:

    def maxProfit(self, k: int, prices: list) -> int:
        if not prices:
            return 0
        n = len(prices)
        index_ = 0  # 天数
        status_ = 0  # 当前状态
        count_ = 0  # 交易次数
        # 如果交易次数大于股票的可交易此处按无限次执行
        if k > n // 2:
            a0, b0 = 0, 0 - prices[0]
            for i in range(1, n):
                a0 = max(a0, b0 + prices[i])
                b0 = max(b0, a0 - prices[i])
            return max(a0, b0)
        d = dict()

        def foo(index, status, count):
            if (index, status, count) in d.keys():
                return d[index, status, count]
            if index == n or count == k:
                return 0
            a, b, c = 0, 0, 0
            a = foo(index + 1, status, count)  # 什么都不干的情况
            if status:
                b = foo(index + 1, 0, count + 1) + prices[index]  # 当前持有但卖出的情况
            else:
                c = foo(index + 1, 1, count) - prices[index]  # 当前不持有但买入的情况
            max_ = max(a, b, c)  # 选择收益最大的
            d[index, status, count] = max_
            return max_  # 返回收益最大的

        r = foo(index_, status_, count_)
        return r

    def run(self):
        k = 7
        prices = [48, 12, 60, 93, 97, 42, 25, 64, 17, 56, 85, 93, 9, 48, 52, 42, 58, 85, 81, 84, 69, 36, 1, 54, 23, 15,
                  72, 15, 11, 94]
        r = self.maxProfit(k, prices)
        print(r)


s = Solution()
s.run()
