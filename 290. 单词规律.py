class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()
        if len(pattern) != len(s_list):  # 如果长度不一样，则肯定不匹配
            return False
        p_dict = dict()
        for i, p in enumerate(pattern):
            p_value = p_dict.get(p)
            if p_value:
                if p_value != s_list[i]:  # 如果和前边同样字符对应的字符串不一样，则不匹配
                    return False
            else:
                if s_list[i] in p_dict.values():  # 如果key没有添加过，但对应位置的值在value出现过则不匹配
                    return False
                p_dict[p] = s_list[i]  # 如果key和对应位置的value都没有添加过，则添加到字典里
        return True

    def wordPattern2(self, pattern: str, s: str) -> bool:
        s_list = s.split()
        if len(pattern) != len(s_list):  # 如果长度不一样，则肯定不匹配
            return False
        p_dict = dict()
        s_dict = dict()
        for i in range(len(pattern)):
            if (p_dict.get(pattern[i]) and p_dict.get(pattern[i]) != s_list[i]) or \
                    (s_dict.get(s_list[i]) and s_dict.get(s_list[i]) != pattern[i]):
                return False
            else:
                p_dict[pattern[i]] = s_list[i]
                s_dict[s_list[i]] = pattern[i]
        return True

    def run(self):
        pattern = "abba"
        s = "dog dog dog dog"
        r = self.wordPattern2(pattern, s)
        print(r)


s = Solution()
s.run()
