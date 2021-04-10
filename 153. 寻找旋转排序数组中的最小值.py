import heapq


class Solution:

    def findMin(self, nums: list) -> int:
        if len(nums) == 0:
            return -1
        start, end = 0, len(nums) - 1
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
        return nums[end]

    def run(self):
        nums = [3, 1, 2]
        r = self.findMin(nums)
        print(r)


s = Solution()
s.run()


class Solution:
    def findMin(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        return heapq.heappop(nums)
