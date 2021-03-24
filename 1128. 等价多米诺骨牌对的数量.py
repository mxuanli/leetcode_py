from collections import defaultdict


class Solution:

    def numEquivDominoPairs2(self, dominoes: list) -> int:
        nums = defaultdict(int)
        r = 0
        for dominoe in dominoes:
            x, y = dominoe[0], dominoe[1]
            if x > y:
                num = x * 10 + y
            else:
                num = y * 10 + x
            r += nums[num]
            nums[num] += 1
        return r

    def numEquivDominoPairs(self, dominoes: list) -> int:
        nums = defaultdict(int)
        r = 0
        for dominoe in dominoes:
            num = tuple(sorted(dominoe))
            r += nums[num]
            nums[num] += 1
        return r

    def run(self):
        dominoes = [[1, 2], [2, 1], [3, 4], [5, 6]]
        r = self.numEquivDominoPairs(dominoes)
        print(r)


s = Solution()
s.run()
