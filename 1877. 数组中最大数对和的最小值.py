class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        r = nums[0] + nums[n-1]
        for i in range(n // 2):
            r = max(r, nums[i] + nums[n - i - 1])
        return r
