class Solution:

    def singleNumber2(self, nums: list) -> int:
        r = 0
        for i in nums:
            r ^= i
        return r

    def singleNumber(self, nums: list) -> int:
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        for i in range(len(nums)):
            if i == 0 and nums[i] != nums[i + 1]:
                return nums[i]
            elif i == len(nums) - 1 and nums[i] != nums[i - 1]:
                return nums[i]
            elif nums[i - 1] != nums[i] and nums[i + 1] != nums[i]:
                return nums[i]
        return 0

    def run(self):
        nums = [2]
        r = self.singleNumber(nums)
        print(r)


s = Solution()
s.run()
