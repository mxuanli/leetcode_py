class Solution:

    def findContentChildren(self, g: list, s: list) -> int:
        # 尽量给孩子分能满足他胃口的最小的饼干
        g.sort()
        s.sort()
        r, gi, si = 0, 0, 0
        while si < len(s) and gi < len(g):
            if s[si] >= g[gi]:  # 如果能满足，就都加一
                r, gi, si = r + 1, gi + 1, si + 1
            else:
                si += 1  # 因为g和s都是从小按大排序，所以不能满足前一个孩子，那也肯定不能满足后边的，就直接跳过
        return r

    def findContentChildren2(self, g: list, s: list) -> int:
        # 尽量把饼干分配给胃口最大的孩子
        g = sorted(g, reverse=True)
        s = sorted(s, reverse=True)
        r, gi, si = 0, 0, 0
        while si < len(s) and gi < len(g):
            if s[si] >= g[gi]:  # 如果能满足，就都加一
                r, gi, si = r + 1, gi + 1, si + 1
            else:
                gi += 1  # 因为g和s都是从大按小排序，如果饼干不能满足孩子，那就没有更大的饼干了，换一个胃口小的孩子
        return r

    def findContentChildren3(self, g: list, s: list) -> int:
        g.sort()
        s.sort()
        gi = 0
        for si in range(len(s)):
            if s[si] >= g[gi]:
                gi += 1
            if gi == len(g):
                return gi
        return gi


    def run(self):
        g = [1, 2, 3]
        s = [1, 1]
        r = self.findContentChildren2(g, s)
        print(r)


s = Solution()
s.run()
