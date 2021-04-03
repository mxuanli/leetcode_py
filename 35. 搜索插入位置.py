class Solution:

    def searchInsert(self, nums: list, target: int) -> int:
        start = 0
        end = len(nums) - 1
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                start = mid
            if nums[mid] > target:
                end = mid
        if nums[start] >= target:
            return start
        if nums[end] <= target:
            return len(nums)
        if nums[end] >= target:
            return end
        return 0

    def run(self):
        nums = [1, 3, 5, 6]
        target = 3
        a = self.searchInsert(nums, target)
        print(a)


s = Solution()
s.run()
