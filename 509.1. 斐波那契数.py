class Solution:

    def fib(self, N: int) -> int:
        if N == 1 or N == 2:
            return 1
        a, b = 0, 1
        for i in range(N):
            a, b = b, a + b
        return a

    def fib2(self, N: int):
        if N == 0:
            return N
        if N == 1:
            return N
        return self.fib(N - 1) + self.fib(N - 2)

    def run(self):
        N = 4
        r = self.fib(N)
        print(r)


s = Solution()
s.run()
