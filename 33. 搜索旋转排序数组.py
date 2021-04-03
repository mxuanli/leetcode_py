class Solution:

    def search(self, nums: list, target: int) -> int:
        # 二分搜索
        if len(nums) == 0:
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            # 如果mid点小于end点，那nums[mid, end]一定是有序的
            if nums[mid] < nums[end]:
                # 如果满足上边条件，并且target在这个有序的区间范围内，则移动start
                if nums[mid] <= target <= nums[end]:
                    start = mid
                else:
                    end = mid
            # 如果mid点大于end点，那nums[start, mid]一定是有序的
            if nums[mid] > nums[end]:
                # 如果满足上边条件，并且target在这个有序的区间范围内，则移动end
                if nums[start] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

    def run(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        r = self.search(nums, target)
        print(r)


s = Solution()
s.run()
