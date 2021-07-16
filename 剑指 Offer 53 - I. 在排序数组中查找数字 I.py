class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r = 0
        for num in nums:
            if num == target:
                r += 1
        return r
