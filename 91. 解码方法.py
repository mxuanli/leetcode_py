class Solution:
    def numDecodings(self, s: str) -> int:
        int_list = [str(i) for i in range(1, 27)]
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(1, len(s) + 1):
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]
            if s[i - 2] != '0' and s[i - 2] + s[i - 1] in int_list:
                dp[i] += dp[i - 2]
        return dp[-1]
