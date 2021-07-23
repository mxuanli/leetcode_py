class Solution:
    """暴力"""

    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        for m in matrix:
            if target in m:
                return True
        return False


class Solution1:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        if n == 0:
            return False
        m = len(matrix[0])
        i, j = 0, m - 1
        while i < n and j >= 0:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                j -= 1
            if matrix[i][j] < target:
                i += 1
        return False
