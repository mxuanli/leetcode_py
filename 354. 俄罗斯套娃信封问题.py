class Solution:
    def maxEnvelopes(self, envelopes: list) -> int:
        n = len(envelopes)
        if n == 0:
            return 0
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        new_envelopes = [i[1] for i in envelopes]
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if new_envelopes[i] > new_envelopes[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def run(self):
        envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
        r = self.maxEnvelopes(envelopes)
        print(r)


s = Solution()
s.run()
