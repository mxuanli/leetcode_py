class Solution:

    def equalSubstring2(self, s: str, t: str, maxCost: int) -> int:
        cost_list = list()
        for i, sv in enumerate(s):
            tv = t[i]
            cost = abs(ord(tv) - ord(sv))
            cost_list.append(cost)
        start, cost, r = 0, 0, 0
        for end in range(len(cost_list)):
            cost += cost_list[end]
            if cost > maxCost:
                cost -= cost_list[start]
                start += 1
                continue
            r = max(r, end - start + 1)
        return r

    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost_list = list()
        # 计算开销
        for i, sv in enumerate(s):
            tv = t[i]
            cost = abs(ord(tv) - ord(sv))
            cost_list.append(cost)
        # 计算花费小于maxCost时的最长窗口
        start, cost, r = 0, 0, 0
        for end in range(len(cost_list)):
            cost += cost_list[end]
            while cost > maxCost:
                cost -= cost_list[start]
                start += 1
                continue
            r = max(r, end - start + 1)
        return r

    def run(self):
        s = "abcd"
        t = "cdef"
        cost = 3
        r = self.equalSubstring(s, t, cost)
        print(r)


s = Solution()
s.run()
