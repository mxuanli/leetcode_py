class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        r_list = [0, 1, 1]
        for i in range(n - 3):
            r_list.append(sum(r_list[-3:]))
        return sum(r_list[-3:])


class Solution1:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        a, b, c = 0, 1, 1
        for i in range(n - 2):
            a, b, c = b, c, a + b + c
        return c
