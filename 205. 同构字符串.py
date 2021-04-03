class Solution:

    def isIsomorphic(self, s: str, t: str) -> bool:
        s_list, s_dict, t_list, t_dict = list(), dict(), list(), dict()
        for index, si in enumerate(s):
            si_value = s_dict.get(si)
            if si_value != None:
                s_list.append(si_value)
            else:
                s_dict[si] = index
                s_list.append(index)
        for index, ti in enumerate(t):
            ti_value = t_dict.get(ti)
            if ti_value != None:
                t_list.append(ti_value)
            else:
                t_dict[ti] = index
                t_list.append(index)
        if len(s_list) != len(t_list):
            return False
        for i in range(len(s_list)):
            if s_list[i] != t_list[i]:
                return False
        return True


    def run(self):
        s = "ab"
        t = "aa"
        r = self.isIsomorphic(s, t)
        print(r)


s = Solution()
s.run()
