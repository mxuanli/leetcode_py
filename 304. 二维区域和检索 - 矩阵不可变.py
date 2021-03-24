class NumMatrix2:

    def __init__(self, matrix: list):
        # 暴力解
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r = 0
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                r += self.matrix[i][j]
        return r


class NumMatrix:

    def __init__(self, matrix: list):
        # 前缀和
        # if not matrix[0][0]:
        if not matrix:
            self.matrix = [[0]]
            return
        n, m = len(matrix), len(matrix[0])
        self.matrix = [[0] * (m + 1) for _ in range(n)]
        for i in range(n):
            for j in range(m):
                self.matrix[i][j + 1] = matrix[i][j] + self.matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r = 0
        for i in range(row1, row2 + 1):
            r += self.matrix[i][col2 + 1] - self.matrix[i][col1]
        return r


matrix1 = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]

matrix = [[[]]]

s = NumMatrix(matrix)
r = s.sumRegion(2, 1, 4, 3)
print(r)
r = s.sumRegion(1, 1, 2, 2)
print(r)
r = s.sumRegion(1, 2, 2, 4)
print(r)
