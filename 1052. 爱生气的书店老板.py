class Solution:

    def maxSatisfied(self, customers: list, grumpy: list, X: int) -> int:
        n = len(customers)
        sum_0, tmp = 0, 0
        r = 0
        start, end = 0, 0
        for end in range(n):
            if grumpy[end] == 0:
                r += customers[end]
            else:
                tmp += customers[end]
            if end - start + 1 == X:
                sum_0 = max(tmp, sum_0)
                if grumpy[start] == 1:
                    tmp -= customers[start]
                start += 1
        r += sum_0
        return r

    def run(self):
        customers = [4, 10, 10]
        grumpy = [1, 1, 0]
        X = 2
        r = self.maxSatisfied(customers, grumpy, X)
        print(r)


s = Solution()
s.run()
