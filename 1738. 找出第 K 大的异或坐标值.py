class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        matrix_xor = [[0] * (n + 1) for _ in range(m + 1)]
        tmp = list()
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                matrix_xor[i][j] = matrix_xor[i - 1][j] ^ matrix_xor[i][j - 1] ^ matrix_xor[i - 1][j - 1] ^ matrix[i - 1][j - 1]
                tmp.append(matrix_xor[i][j])
        tmp.sort(reverse=True)
        return tmp[k - 1]
