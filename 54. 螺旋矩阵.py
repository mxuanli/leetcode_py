class Solution:

    def spiralOrder(self, matrix: list) -> list:
        r = list()
        n = len(matrix)
        m = len(matrix[0])
        r = self.foo(r, matrix, n, m)
        return r

    def foo(self, r: list, matrix, n, m):
        if n <= 0 or m <= 0:
            return r
        if n == 1:
            r += matrix[0]
            return r
        if m == 1:
            for m in matrix:
                r.append(m[0])
            return r
        r += matrix[0]
        n -= 1
        matrix = matrix[1:]
        for i in range(n - 1):
            r.append(matrix[i][-1])
            matrix[i] = matrix[i][:-1]
        m -= 1
        r += matrix[-1][::-1]
        matrix = matrix[:-1]
        n -= 1
        for i in range(n - 1, -1, -1):
            r.append(matrix[i][0])
            matrix[i] = matrix[i][1:]
        m -= 1
        self.foo(r, matrix, n, m)
        return r

    def run(self):
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        r = self.spiralOrder(matrix)
        print(r)


s = Solution()
s.run()
