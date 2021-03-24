class Solution:

    def calculate(self, s: str) -> int:
        r = 0
        sign = 1
        n = len(s)
        i = 0
        stack = list()
        tmp = 0
        while i < n:
            if s[i].isdigit():
                tmp = tmp * 10 + int(s[i])
            elif s[i] == "+":
                r += tmp * sign
                tmp = 0
                sign = 1
            elif s[i] == "-":
                r += tmp * sign
                tmp = 0
                sign = -1
            elif s[i] == "(":
                stack.append(r)
                stack.append(sign)
                tmp = 0
                r = 0
                sign = 1
            elif s[i] == ")":
                r += tmp * sign
                tmp = 0
                sign = stack.pop()
                r *= sign
                r += stack.pop()
            i += 1
        r += sign * tmp
        return r

    def calculate2(self, s: str) -> int:
        r = 0
        sign = 1
        n = len(s)
        i = 0
        stack = list()
        while i < n:
            if s[i] == " ":
                i += 1
                continue
            elif s[i] == "+":
                sign = 1
                i += 1
            elif s[i] == "-":
                sign = -1
                i += 1
            elif s[i] == "(":
                stack.append(r)
                stack.append(sign)
                sign = 1
                r = 0
                i += 1
            elif s[i] == ")":
                sign = stack.pop()
                tmp = stack.pop()
                r *= sign
                r = tmp + r
                i += 1
            elif s[i].isdigit():
                tmp = int(s[i])
                i += 1
                while i < n and s[i].isdigit():
                    tmp *= 10
                    tmp += int(s[i])
                    i += 1
                tmp *= sign
                r += tmp
        return r

    def run(self):
        s = "- (3 + (4 + 5))"
        r = self.calculate(s)
        print(r)


s = Solution()
s.run()
