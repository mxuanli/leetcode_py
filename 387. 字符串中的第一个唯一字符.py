from collections import defaultdict


class Solution(object):

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i, v in enumerate(s):
            if v not in s[:i] + s[i+1:]:
                return i
        return -1

    def firstUniqChar2(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_dict = defaultdict(int)
        for i in s:
            s_dict[i] += 1
        for i, v in enumerate(s):
            if s_dict[v] == 1:
                return i
        return -1

    def run(self):
        s = "lovveleettccodde"
        r = self.firstUniqChar2(s)
        print(r)


s = Solution()
s.run()
