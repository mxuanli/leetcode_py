class Solution:

    def removeDuplicates1(self, S: str) -> str:
        flag = True
        while flag:
            flag = False
            i = len(S) - 1
            while i > 0:
                if S[i] == S[i - 1]:
                    S = S[:i - 1] + S[i + 1:]
                    i -= 2
                    flag = True
                i -= 1
        return S

    def removeDuplicates(self, S: str) -> str:
        """
        abba
        字符ab会先被添加到栈内，
        当遍历到第二个b的时候，栈顶字符也为b，所以删除掉，
        删除掉后栈顶元素会变成a，遍历到第二个a后，a也会被删掉
        """
        stack = list()
        for s in S:
            if stack and stack[-1] == s:
                stack.pop()
            else:
                stack.append(s)
        return ''.join(stack)

    def run(self):
        S = "aaaaaaaa"
        r = self.removeDuplicates(S)
        print(r)


s = Solution()
s.run()
