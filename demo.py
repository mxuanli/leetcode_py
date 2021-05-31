class Solution1:
    def maxValue(self, n: str, x: int) -> str:
        str_x = str(x)
        r = int(n + str_x)
        len_n = len(n)
        j = 0
        if n[0] == "-":
            j = 1
        for i in range(j, len_n):
            tmp = n[:i] + str_x + n[i:]
            r = max(r, int(tmp))
        return str(r)

class Solution:
    def maxValue(self, n: str, x: int) -> str:
        flag = True
        n1 = n
        if n[0] == "-":
            flag = False
            n1 = n[1:]
        l1 = list(n1)
        x = str(x)
        l2 = sorted(set(l1),key=l1.index)
        k = False
        for v in l2:
            if flag and v <= x:
                k = True
                break
            elif not flag and v >= x:
                k = True
                break
        if flag:
            if k:
                i = n.find(v)
            else:
                i = 0
        else:
            if k:
                i = len(n) - (n[::-1].find(v))
            else:
                i = len(n)
        return n[:i] + x + n[i:]



s = Solution()
r = s.maxValue("-5646", 7)
print(r)

b = "452728"
l1 = list(b)
l2 = sorted(set(l1),key=l1.index)
print(l2)
