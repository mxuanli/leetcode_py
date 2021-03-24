class Solution:

    def findMin(self, nums: list) -> int:
        if len(nums) == 0:
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            while start < end and nums[end] == nums[end - 1]:
                end -= 1
            while start < end and nums[start] == nums[start + 1]:
                start += 1
            mid = start + (end - start) // 2
            if nums[mid] <= nums[end]:
                end = mid
            else:
                start = mid
        if nums[start] < nums[end]:
            return nums[start]
        return nums[end]

    def run(self):
        nums = [1, 3, 5]
        r = self.findMin(nums)
        print(r)


s = Solution()
s.run()
