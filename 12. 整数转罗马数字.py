class Solution0:
    def intToRoman(self, num: int) -> str:
        roman_hash = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        roman_hash_keys = roman_hash.keys()
        r = ""
        while num > 0:
            for roman in roman_hash_keys:
                if num >= roman:
                    r += roman_hash.get(roman)
                    num -= roman
                    break
        return r


class Solution:
    def intToRoman(self, num: int) -> str:
        roman_hash = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        roman_hash_keys = roman_hash.keys()
        r = ""
        for roman in roman_hash_keys:
            if num // roman > 0:
                roman_count = num // roman
                r += roman_hash.get(roman) * roman_count
                num %= roman
        return r


s = Solution()
r = s.intToRoman(3998)
print(r)
