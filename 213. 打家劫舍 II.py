class Solution:

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        a, b = 0, 0  # b存储上一个值，a存储上上一个值和当前最大值
        for i in range(len(nums) - 1):
            a, b = b, max(b, a + nums[i])
        a1, b1 = 0, 0
        for i in range(1, len(nums)):
            a1, b1 = b1, max(b1, a1 + nums[i])
        return max(b, b1)
