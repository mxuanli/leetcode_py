class Solution:

    def removeDuplicates(self, nums: list) -> int:
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] == nums[i - 1]:
                del nums[i]
        return len(nums)

    def run(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        r = self.removeDuplicates(nums)
        print(r)


s = Solution()
s.run()
