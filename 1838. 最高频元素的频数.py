class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        r = 1
        if nums == 1:
            return r
        nums.sort()
        start, end = 0, 0
        diff = 0
        while end < n:
            diff = diff + (end - start) * (nums[end] - nums[end - 1])
            if diff <= k:
                r = max(r, end - start + 1)
            while diff > k:
                diff = diff - (nums[end] - nums[start])
                start += 1
            end += 1
        return r
