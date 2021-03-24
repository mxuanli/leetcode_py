from collections import defaultdict


class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) == 0 or len(s2) < len(s1):
            return False
        frep = defaultdict(int)
        for s in s1:
            frep[s] += 1
        left, right, count = 0, 0, len(s1)
        for right, s in enumerate(s2):
            if frep[s] >= 1:
                count -= 1
            frep[s] -= 1
            if count == 0:
                return True
            if right + 1 - left == len(s1):
                s_left = s2[left]
                if frep[s_left] >= 0:
                    count += 1
                frep[s_left] += 1
                left += 1
        return False

    def run(self):
        s1 = "ab"
        s2 = "eidboaoo"
        result = self.checkInclusion2(s1, s2)
        print(result)
        s1 = "abc"
        s2 = "ccccbbbbaaaa"
        result = self.checkInclusion2(s1, s2)
        print(result)

    def checkInclusion2(self, s1: str, s2: str) -> bool:
        if len(s1) == 0 or len(s2) < len(s1):
            return False
        freq = defaultdict(int)
        for c in s1:
            freq[c] += 1
        left, right, count = 0, 0, len(s1)
        for right, c in enumerate(s2):
            if freq[c] >= 1:
                count -= 1
            freq[c] -= 1
            if count == 0:
                return True
            if right + 1 - left == len(s1):
                if freq[s2[left]] >= 0:
                    count += 1
                freq[s2[left]] += 1
                left += 1
        return False


s = Solution()
s.run()
