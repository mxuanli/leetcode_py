class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        # dp[i][j][k]表示第i天，有j个A且结尾有k个L可获得出勤奖励的数量，0<=j<=2，0<=k<=3
        dp = [[[0, 0, 0], [0, 0, 0]]for _ in range(n + 1)]
        dp[0][0][0] = 1  # 边界
        # 状态都由dp[i][x][x]转换而来，所以dp长度为n+1，循环范围为1,n
        for i in range(1, n + 1):
            # 最后一位为P（到场），A数量不变，P数量+1，结尾L清空，k=0
            for j in range(2):
                for k in range(3):
                    dp[i][j][0] = (dp[i][j][0] + dp[i - 1][j][k]) % MOD
            # 最后一位为L（迟到），A数量不变，P数量不变，L+1，j<=2，k<=2
            for j in range(2):
                for k in range(1, 3):
                    dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j][k - 1]) % MOD
            # 最后一位为A（缺勤），A数量+1，P不变，结尾L清空，此时j<2，此之前A的数量必须为0
            for k in range(3):
                dp[i][j][0] = (dp[i][j][0] + dp[i - 1][0][k]) % MOD
        r = 0
        for j in range(2):
            for k in range(3):
                r += dp[n][j][k]
        return r % MOD
