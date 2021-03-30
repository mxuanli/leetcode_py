from collections import defaultdict


class Solution:

    def isUnique2(self, astr: str) -> bool:
        astr = sorted(astr)
        for i in range(len(astr) - 1):
            if astr[i] == astr[i + 1]:
                return False
        return True

    def isUnique3(self, astr: str) -> bool:
        cur = defaultdict(int)
        for i in astr:
            if cur[i] > 0:
                return False
            cur[i] += 1
        return True

    def isUnique(self, astr: str) -> bool:
        cur = [0] * 24
        for i in astr:
            print(ord(i) - ord('a'))
            if cur[ord(i) - ord('a')] > 0:
                return False
            cur[ord(i) - ord('a')] += 1
        return True

    def run(self):
        s = "iluhwpyk"
        r = self.isUnique(s)
        print(r)


s = Solution()
s.run()
