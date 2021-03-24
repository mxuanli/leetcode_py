class Solution:

    def minCostClimbingStairs(self, cost: list) -> int:
        # 存储到每一步的最小值，最后从倒数两个选取最小的
        n = len(cost)
        r = [0] * n
        r[0], r[1] = cost[0], cost[1]
        i = 2
        while i < n:
            r[i] += cost[i] + min(r[i - 1], r[i - 2])
            i += 1
        return min(r[-1], r[-2])

    def minCostClimbingStairs2(self, cost: list) -> int:
        # 每一步需要消耗的体力为前一步或者前两步较小的值加上本步的值，cost[i] + min(r[i - 1], r[i - 2])
        # 存储到每一步的最小值，最后从倒数两个选取最小的
        n = len(cost)
        r = [0] * n
        r[0], r[1] = cost[0], cost[1]
        for i in range(2, n):
            r[i] += cost[i] + min(r[i - 1], r[i - 2])
        return min(r[-1], r[-2])

    def run(self):
        cost = [0, 0, 1, 1, 1, 2]
        r = self.minCostClimbingStairs2(cost)
        print(r)


s = Solution()
s.run()
