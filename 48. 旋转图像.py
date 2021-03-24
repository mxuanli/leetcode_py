import copy


class Solution:

    def rotate2(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(i, m):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            for j in range(m // 2, m):
                matrix[i][j], matrix[i][m - j - 1] = matrix[i][m - j - 1], matrix[i][j]

    def rotate(self, matrix: list) -> None:
        n = len(matrix)
        m = copy.deepcopy(matrix)
        for i in range(n):
            for j in range(n):
                matrix[j][n - i - 1] = m[i][j]

    def run(self):
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        self.rotate(matrix)


s = Solution()
s.run()
