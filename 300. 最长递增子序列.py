

class Solution:

    def lengthOfLIS(self, nums: list) -> int:
        n = len(nums)
        if nums == 0:
            return 0
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def run(self):
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        r = self.lengthOfLIS(nums)
        print(r)


s = Solution()
s.run()
