class Solution:
    def arrayPairSum(self, nums: list) -> int:
        return sum(sorted(nums)[::2])

    def run(self):
        nums = [6, 2, 6, 5, 1, 2]
        r = self.arrayPairSum(nums)
        print(r)


s = Solution()
s.run()
