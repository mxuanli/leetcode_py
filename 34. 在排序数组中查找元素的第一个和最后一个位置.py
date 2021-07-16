class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = -1, -1
        n = len(nums)
        for i in range(n):
            if start == -1 and nums[i] == target:
                start = i
            if start != -1 and nums[i] == target:
                end = i
            if end != -1 and nums[i] != target:
                break
        return [start, end]
