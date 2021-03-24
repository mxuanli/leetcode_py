
class Solution:

    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [n] * n
        for i in range(n):
            if self.is_palindrome(s[:i + 1]):
                dp[i] = 0
                continue
            for j in range(i):
                if self.is_palindrome(s[j + 1: i + 1]):
                    dp[i] = min(dp[i], dp[j] + 1)
        r = dp[-1]
        return r

    @staticmethod
    def is_palindrome(s: str) -> bool:
        if s == s[::-1]:
            return True
        return False

    def run(self):
        s = "cdd"
        r = self.minCut(s)
        print(r)


s = Solution()
s.run()
