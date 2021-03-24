class Solution:

    def searchMatrix(self, matrix: list, target: int) -> bool:
        # 转换为一维数组
        list_o = list()
        for list_i in matrix:
            list_o += list_i
        # 二分查找
        start = 0
        end = len(list_o) - 1
        if len(list_o) == 0:
            return False
        if list_o[start] == target:
            return True
        if list_o[end] == target:
            return True
        while start + 1 < end:
            mid = (start + end) // 2
            if list_o[mid] == target:
                return True
            if list_o[mid] > target:
                end = mid
            if list_o[mid] < target:
                start = mid
        return False

    def searchMatrix2(self, matrix: list, target: int) -> bool:
        if len(matrix) == 0:
            return False
        # 二分查找
        start = 0
        len_target = len(matrix[0])
        len_m = len(matrix) * len(matrix[0]) - 1
        end = len_m
        if len_m < 0:
            return False
        if matrix[0][0] == target:
            return True
        if matrix[-1][-1] == target:
            return True
        while start + 1 < end:
            mid = (start + end) // 2
            # 获取到对应的值
            matrix_mid = matrix[mid // len_target][mid % len_target]
            if matrix_mid == target:
                return True
            if matrix_mid > target:
                end = mid
            if matrix_mid < target:
                start = mid
        return False

    def run(self):
        matrix = [[1, 3, 5]]
        target = 0
        r = self.searchMatrix2(matrix, target)
        print(r)


s = Solution()
s.run()
