class Solution:

    def twoSum(self, nums: list, target: int) -> list:
        tmp = dict()
        for i, v in enumerate(nums):
            r = target - v
            if r in tmp:
                return [i, tmp[r]]
            else:
                tmp[v] = i

    def run(self):
        nums = [2, 7, 11, 15]
        target = 9
        r = self.twoSum(nums, target)
        print(r)


s = Solution()
s.run()
