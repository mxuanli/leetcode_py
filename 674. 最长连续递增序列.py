class Solution:
    def findLengthOfLCIS(self, nums: list) -> int:
        n = len(nums)
        if n <= 1:
            return n
        max_count = 0
        start, end = 0, 1
        while end < n:
            while end < n and nums[end - 1] < nums[end]:
                end += 1
            max_count = max(max_count, end - start)
            start = end
            end += 1
        return max_count

    def run(self):
        nums = [1, 3, 5, 4, 7]
        r = self.findLengthOfLCIS(nums)
        print(r)


s = Solution()
s.run()
