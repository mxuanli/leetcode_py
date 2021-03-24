class Solution:

    def checkPossibility(self, nums: list) -> bool:
        count = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                count += 1
                if count > 1:
                    return False
                if i == 1 or i > 1 and nums[i] > nums[i - 2]:
                    nums[i - 1] = nums[i]
                if i > 1 and nums[i] < nums[i - 2]:
                    nums[i] = nums[i - 1]
        return True

    def run(self):
        nums = [3, 4, 2, 3]
        r = self.checkPossibility(nums)
        print(r)


s = Solution()
s.run()
