from collections import defaultdict


class Solution:

    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        for i in set(s):
            if s.count(i) < k:
                return max([self.longestSubstring(i, k) for i in s.split(i)])
        return len(s)

    def run(self):
        s = "aaabb"
        k = 3
        r = self.longestSubstring(s, k)
        print(r)


s = Solution()
s.run()
