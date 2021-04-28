class Solution:
    def combinationSum4(self, nums, target) -> int:
        self.dp = [-1] * (target + 1)
        self.dp[0] = 1
        return self.foo(nums, target)

    def foo(self, nums, target) -> int:
        if target < 0:
            return 0
        if self.dp[target] != -1:
            return self.dp[target]
        res = 0
        for num in nums:
            res += self.foo(nums, target - num)
        self.dp[target] = res
        return res


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(target + 1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i - num]
        return dp[target]
