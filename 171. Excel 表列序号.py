class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        dict_tmp = dict()
        num = 1
        for i in range(65, 91):
            dict_tmp[chr(i)]  = num
            num += 1
        r = 0
        tmp = 1
        for c in columnTitle[::-1]:
            k = dict_tmp[c]
            r += k * tmp
            tmp *= 26
        return r
