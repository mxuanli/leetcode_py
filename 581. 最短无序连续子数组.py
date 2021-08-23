class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_sort = sorted(nums)
        if nums == nums_sort:
            return 0
        start = 0
        while nums_sort[start] == nums[start]:
            start += 1
        end = len(nums) - 1
        while nums_sort[end] == nums[end]:
            end -= 1
        return end - start + 1
