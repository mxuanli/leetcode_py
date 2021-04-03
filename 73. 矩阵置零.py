import copy


class Solution:
    def setZeroes2(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        zero = {"x": set(), "y": set()}
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zero["x"].add(i)
                    zero["y"].add(j)
        for i in range(n):
            for j in range(m):
                if i in zero["x"] or j in zero["y"]:
                    matrix[i][j] = 0
        print(matrix)

    def setZeroes(self, matrix: list) -> None:
        n = len(matrix)
        m = len(matrix[0])
        flag = False
        for i in range(n):
            if matrix[i][0] == 0:
                flag = True
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(n - 1, -1, -1):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if flag:
                matrix[i][0] = 0
        print(matrix)

    def run(self):
        matrix = [[1,1,1],[1,0,1],[1,1,1]]
        self.setZeroes(matrix)


s = Solution()
s.run()
