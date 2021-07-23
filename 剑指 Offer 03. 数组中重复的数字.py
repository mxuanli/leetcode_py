class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums.sort()
        r = 0
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                r = nums[i]
                break
        return r
