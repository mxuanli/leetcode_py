class Solution:
    def fib(self, n: int) -> int:
        if n == 1 or n == 2:
            return 1
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a % (10 ** 9 + 7)
