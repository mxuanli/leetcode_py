from collections import defaultdict


class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        dict_s = defaultdict(int)
        start = 0
        n = len(s)
        max_r = 0
        for end in range(n):
            dict_s[s[end]] += 1
            max_l = max(dict_s.values())
            if (end - start + 1) > (max_l + k):
                dict_s[s[start]] -= 1
                start += 1
            else:
                max_r = max(max_r, end - start + 1)
        return max_r

    def run(self):
        s = "AABABBA"
        k = 1
        r = self.characterReplacement(s, k)
        print(r)


s = Solution()
s.run()
