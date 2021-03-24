class Solution:

    def isToeplitzMatrix2(self, matrix: list) -> bool:
        n, m = len(matrix), len(matrix[0])
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False
        return True

    def isToeplitzMatrix(self, matrix: list) -> bool:
        n, m = len(matrix), len(matrix[0])
        for i in range(0, n - 1):
            for j in range(0, m - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True

    def run(self):
        matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
        r = self.isToeplitzMatrix(matrix)
        print(r)


s = Solution()
s.run()
