class Solution:

    def flipAndInvertImage2(self, A: list) -> list:
        n, m = len(A), len(A[0])
        for i in range(n):
            for j in range(m // 2):
                A[i][j], A[i][m - j - 1] = A[i][m - j - 1], A[i][j]
            for j in range(m):
                A[i][j] = A[i][j] ^ 1
        return A

    def flipAndInvertImage(self, A: list) -> list:
        n, m = len(A), len(A[0])
        for i in range(n):
            a, b = 0, m - 1
            while a < b:
                if A[i][a] == A[i][b]:
                    A[i][a] ^= 1
                    A[i][b] ^= 1
                a += 1
                b -= 1
            if a == b:
                A[i][a] ^= 1
        return A

    def run(self):
        A = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
        r = self.flipAndInvertImage(A)
        print(r)


s = Solution()
s.run()
