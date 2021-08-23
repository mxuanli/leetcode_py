class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        move_list = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # 四个方向移动
        mod = 10 ** 9 + 7

        @lru_cache(None)  # 记忆化
        def foo(m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
            if startRow < 0 or startRow >= m or startColumn < 0 or startColumn >= n:  # 越界
                return 1
            if maxMove <= 0:  # 没步数
                return 0
            r = 0
            for x, y in move_list:
                r += foo(m, n, maxMove - 1, startRow + x, startColumn + y)  # 四个方向移动
            return r

        r = foo(m, n, maxMove, startRow, startColumn)
        return r % mod
