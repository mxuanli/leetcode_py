

class Solution:

    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        db = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(n + 1):
            db[0][i] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if t[i - 1] == s[j - 1]:
                    db[i][j] = db[i - 1][j - 1] + db[i][j - 1]
                else:
                    db[i][j] = db[i][j - 1]
        return db[-1][-1]

    def run(self):
        s = "babgbag"
        t = "bag"
        r = self.numDistinct(s, t)
        print(r)


s = Solution()
s.run()
