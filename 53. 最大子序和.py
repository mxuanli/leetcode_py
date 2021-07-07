class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n  # dp[i]表示前i个元素的最大子序和
        dp[0] = nums[0]  # 边界条件，第一个元素的最大子序和为它自己
        for i in range(1, n):
            if dp[i - 1] > 0:
                dp[i] = dp[i - 1] + nums[i]  # 如果前边元素的最大子序和是正数，就相加
            else:
                dp[i] = nums[i]  # 如果前边元素的最大子序和是负数，最大子序和就是当前元素
        return max(dp)


class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        r, a = nums[0], nums[0]
        for i in range(1, n):
            if a > 0:
                a = a + nums[i]  # 如果前边元素的最大子序和是正数，就相加
            else:
                a = nums[i]  # 如果前边元素的最大子序和是负数，最大子序和就是当前元素
            r = max(r, a)
        return r
