

class Solution:

    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        int_str = "0123456789"
        sign_str = "-+"
        r, i, t = 0, 0, 1
        for i, j in enumerate(s):
            if j != " ":
                break
        if s[i] not in sign_str and s[i] not in int_str:
            return 0
        if s[i] in sign_str:
            if s[i] == "-":
                t = 0
            i += 1
        for k in s[i:]:
            if k in int_str:
                r *= 10
                r += int(k)
            else:
                break
        if t:
            if r > (2**31)-1:
                r = (2**31)-1
        else:
            if r > (2**31):
                r = (2**31)
            r = 0 - r
        return r

    def run(self):
        a = "  0000000000012345678"
        r = self.myAtoi(a)
        print(r)


s = Solution()
s.run()
