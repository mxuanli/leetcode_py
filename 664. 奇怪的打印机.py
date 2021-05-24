class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]  # 表示区间 s[i: j] 的最小操作数
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    r_ij = 9999
                    for k in range(i, j):
                        r_ij = min(r_ij, dp[i][k] + dp[k + 1][j])
                    dp[i][j] = r_ij
        return dp[0][n - 1]
