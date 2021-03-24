

class Solution:

    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1
        return self.fib(N-1) + self.fib(N-2)

    def fib2(self, N):
        i, j = 0, 1
        for k in range(N):
            i, j = j, i + j
        return i

    def run(self):
        N = 10
        r = self.fib2(N)
        print(r)


s = Solution()
s.run()
