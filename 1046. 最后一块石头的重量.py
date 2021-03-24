class Solution:

    def lastStoneWeight(self, stones: list) -> int:
        while len(stones) >= 2:
            stones.sort()
            y = stones[-1]
            x = stones[-2]
            stones = stones[:-2]
            if x != y:
                stones.append(y-x)
        if len(stones) == 0:
            return 0
        return stones[0]

    def run(self):
        stones = [2, 7, 4, 1, 8, 1]
        r = self.lastStoneWeight(stones)
        print(r)


s = Solution()
s.run()
