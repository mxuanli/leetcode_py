class Solution:

    def findMaxConsecutiveOnes2(self, nums: list) -> int:
        count, r = 0, 0
        i, n = 0, len(nums)
        while i < n:
            while i < n and nums[i] == 0:
                i += 1
                count = 0
            if i < n and nums[i] == 1:
                count += 1
                r = max(count, r)
            i += 1
        return r

    def findMaxConsecutiveOnes(self, nums: list) -> int:
        count, r = 0, 0
        for i in nums:
            if i == 1:
                count += 1
            if i == 0:
                r = max(r, count)
                count = 0
        r = max(r, count)
        return r

    def run(self):
        nums = [1]
        r = self.findMaxConsecutiveOnes(nums)
        print(r)


s = Solution()
s.run()
