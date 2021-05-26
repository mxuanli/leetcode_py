class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = list()
        r = ""
        for i in s:
            if i == "(":
                stack.append(r)
                r = ""
            elif i == ")":
                r = r[::-1]
                r = stack.pop() + r
            else:
                r += i
        return r
