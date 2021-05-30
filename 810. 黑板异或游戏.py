class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 0:
            return True
        r = 0
        for num in nums:
            r ^= num
        return r == 0
