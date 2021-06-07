class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        l = len(strs)
        # dp[i][j][k]，在第i个子集，最多有j个0和k个1
        dp = [[[0 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(l + 1)]
        """
        边界：
        i == 0时，dp[i][j][k] = 0
        状态转移方程：
        如果i < zero，k < one，dp[i][j][k = ]dp[i−1][j][k]
        如果j >= zero，k >= one，dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-zero][k-one]+1)
        """
        for i in range(1, l + 1):
            one = strs[i - 1].count("1")
            zero = strs[i - 1].count("0")
            for j in range(m + 1):
                for k in range(n + 1):
                    dp[i][j][k] = dp[i - 1][j][k]
                    if j >= zero and k >= one:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - zero][k - one] + 1)
        return dp[l][m][n]
