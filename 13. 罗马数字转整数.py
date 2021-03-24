class Solution:

    def romanToInt(self, s: str) -> int:
        a = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        r = 0
        si = 0
        while si < len(s)-1:
            if a.get(s[si]) < a.get(s[si+1]):
                r += a.get(s[si+1]) - a.get(s[si])
                si += 1
            else:
                r += a.get(s[si])
            si += 1
        if si == len(s)-1:
            r += a.get(s[si])
        return r

    def romanToInt2(self, s: str) -> int:
        # 如果左边小于右边，就相减，如果左边大于右边就相加
        a = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        r = 0
        for si in range(len(s)-1):
            if a.get(s[si]) < a.get(s[si + 1]):
                r -= a.get(s[si])
            else:
                r += a.get(s[si])
        return r + a.get(s[-1])

    def run(self):
        s = "IV"
        r = self.romanToInt2(s)
        print(r)


s = Solution()
s.run()
