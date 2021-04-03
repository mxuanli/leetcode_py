

class Solution:
    def partition(self, s: str) -> list:
        res = list()
        path = list()
        self.backtrack(s, res, path)
        return res

    def backtrack1(self, s, res, path):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s) + 1):
            if self.is_palindrome(s[:i]):
                path_tmp = path + [s[:i]]
                self.backtrack(s[i:], res, path_tmp)

    def backtrack(self, s, res, path):
        if not s:
            res.append(path[:])
            return
        for i in range(1, len(s) + 1):
            if self.is_palindrome(s[:i]):
                path.append(s[:i])
                self.backtrack(s[i:], res, path)
                path.pop()

    def is_palindrome(self, s):
        if s == s[::-1]:
            return True
        return False

    def run(self):
        s = "aab"
        r = self.partition(s)
        print(r)


s = Solution()
s.run()
