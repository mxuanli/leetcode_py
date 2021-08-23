class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]  # 以i为结尾，差值为diff时的等差子序列
        r = 0
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += dp[j][diff] + 1  # j < i，如果差值相等就相当于在dp[i][diff]基础上多加了dp[j][diff] + 1个等差子序列
                if dp[j][diff]:
                    r += dp[j][diff]
        return r
