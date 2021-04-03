class Solution:

    def removeDuplicateLetters(self, s: str) -> str:
        r_list = list()
        for i, v in enumerate(s):
            if v in r_list:
                continue
            """
            从后边删除比当前值字典序小且还会在后边出现的字符，直到不符合条件的退出
            "bcabc"
            遍历到a的时候，a前边的c因为字典序小于a，且还会在后边出现，所以会给它删除了
            """
            while r_list and v < r_list[-1] and r_list[-1] in s[i:]:
                r_list.pop()
            r_list.append(v)
        r = "".join(r_list)
        return r

    def run(self):
        s = "bcabc"
        r = self.removeDuplicateLetters(s)
        print(r)


s = Solution()
s.run()
