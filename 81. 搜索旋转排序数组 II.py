class Solution:

    def search(self, nums: list, target: int) -> bool:
        if len(nums) == 0:
            return False
        start, end = 0, len(nums)-1
        while start + 1 < end:
            while start < end and nums[start] == nums[start+1]:
                start += 1
            while start < end and nums[end] == nums[end-1]:
                end -= 1
            mid = start + (end - start) // 2
            if nums[mid] < nums[end]:
                if nums[mid] <= target <= nums[end]:
                    start = mid
                else:
                    end = mid
            if nums[mid] > nums[end]:
                if nums[start] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid
        if nums[start] == target or nums[end] == target:
            return True
        return False

    def run(self):
        nums = [2, 5, 6, 0, 0, 1, 2]
        target = 0
        r = self.search(nums, target)
        print(r)


s = Solution()
s.run()


class Solution1:
    # offer消失法
    def search(self, nums: List[int], target: int) -> bool:
        return target in nums
