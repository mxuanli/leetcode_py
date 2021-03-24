class Solution:

    def transpose(self, matrix: list) -> list:
        n, m = len(matrix), len(matrix[0])
        r = [[1] * n for i in range(m)]
        for i in range(n):
            for j in range(m):
                r[j][i] = matrix[i][j]
        return r

    def run(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        r = self.transpose(matrix)
        print(r)


s = Solution()
s.run()
