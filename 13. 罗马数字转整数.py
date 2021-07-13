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


class Solution10515:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }
        r = 0
        while s:
            if roman_dict.get(s[:2]):
                r += roman_dict[s[:2]]
                s = s[2:]
            elif roman_dict.get(s[:1]):
                r += roman_dict[s[:1]]
                s = s[1:]
        return r


class Solution10713:
    def romanToInt(self, s: str) -> int:
        roman_dict = {"I": 1,
                      "IV": 4,
                      "V": 5,
                      "IX": 9,
                      "X": 10,
                      "XL": 40,
                      "L": 50,
                      "XC": 90,
                      "C": 100,
                      "CD": 400,
                      "D": 500,
                      "CM": 900,
                      "M": 1000
                      }
        i = 0
        n = len(s)
        r = 0
        while i < n:
            if i < n - 1 and roman_dict.get(s[i: i + 2]):
                r += roman_dict[s[i: i + 2]]
                i += 2
            else:
                r += roman_dict[s[i]]
                i += 1
        return r