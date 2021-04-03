from sortedcontainers import SortedList


class Solution:

    def longestSubarray(self, nums: list, limit: int) -> int:
        n = len(nums)
        if n == 1:
            return 1
        start, end = 0, 1
        s = SortedList()
        r = 0
        for end in range(n):
            s.add(nums[end])
            if s[-1] - s[0] > limit:
                s.remove(nums[start])
                start += 1
        r = max(r, end - start + 1)
        return r

    def run(self):
        nums = [8,2,4,7]
        limit = 4
        r = self.longestSubarray(nums, limit)
        print(r)


s = Solution()
s.run()
