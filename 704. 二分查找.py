class Solution:
    def search(self, nums: list, target: int) -> int:
        start = 0
        end = len(nums) - 1
        if target == nums[start]:
            return start
        if target == nums[end]:
            return end
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                start = mid
            if nums[mid] > target:
                end = mid
        return -1

    def run(self):
        nums = [-1, 0, 3, 5, 9, 12]
        target = 9
        r = self.search(nums, target)
        print(r)

s = Solution()
s.run()
