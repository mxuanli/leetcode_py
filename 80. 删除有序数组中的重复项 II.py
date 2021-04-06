class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        tmp = 1
        i = len(nums) - 1
        while i > 0:
            while i > 0 and nums[i] == nums[i - 1]:
                tmp += 1
                i -= 1
                if tmp > 2:
                    del nums[i]
            else:
                tmp = 1
            i -= 1
        return len(nums)
