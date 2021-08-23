class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        r = 0
        n = len(nums)
        for i in range(n - 1):
            diff = nums[i + 1] - nums[i]
            for j in range(i + 1, n - 1):
                if nums[j + 1] - nums[j] == diff:
                    r += 1
                else:
                    break
        return r
