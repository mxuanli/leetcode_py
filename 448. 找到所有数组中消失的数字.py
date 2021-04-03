class Solution:

    def findDisappearedNumbers2(self, nums: list) -> list:
        r = list()
        nums_set = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in nums_set:
                r.append(i)
        return r

    def findDisappearedNumbers(self, nums: list) -> list:
        for i in nums:
            if nums[abs(i) - 1] > 0:
                nums[abs(i) - 1] *= -1
        r = list()
        for i, v in enumerate(nums):
            if v > 0:
                r.append(i + 1)
        return r

    def run(self):
        nums = [4, 3, 2, 7, 8, 2, 3, 1]
        r = self.findDisappearedNumbers(nums)
        print(r)


s = Solution()
s.run()

