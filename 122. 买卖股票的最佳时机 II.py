
class Solution:

    def maxProfit(self, prices: list) -> int:
        r = 0
        a, b = 0, 0 - prices[0]  # a，当前持有；b，当前不持有
        for i in prices[1:]:
            a = max(a, b + i)
            b = max(b, a - i)
            r = max(a, b)
        return r

    def run(self):
        prices = [1,2,3,4,5]
        r = self.maxProfit(prices)
        print(r)


s = Solution()
s.run()
