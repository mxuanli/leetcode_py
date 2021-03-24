class UnionFindSet:

    def __init__(self, N):
        self.father = dict()
        self.count = N

    def find(self, x):
        # 查找
        root = x
        while self.father.get(root) is not None:
            root = self.father[root]
        # 压缩
        while x != root:
            father_root = self.father[x]
            self.father[x] = root
            x = father_root
        return root

    def union(self, x, y):
        # 合并
        xf = self.find(x)
        yf = self.find(y)
        if xf != yf:
            self.father[xf] = yf
            self.count -= 1


class Solution:

    def regionsBySlashes(self, grid: list) -> int:
        """
        一个格子分为四个三角形，每个三角形给一个id，分别是0123
        如果是/则0和3连通，1和2连通；如果是\\则0和1连通，2和3连通
        如果格子所在的行大于一，则当前格子的0需要和上边格子的2连通；
        如果格子的列大于一，则当前格子的3需要和上一个格子的1连通；
          0
        3  1
         2
        :param grid:
        :return:
        """
        n = len(grid)
        ufs = UnionFindSet(n * n * 4)
        for row in range(n):
            # 行
            line = grid[row]
            for col in range(n):
                # 列
                g = line[col]
                if row > 0:
                    # 合并当前格子的2和上边格子的0
                    x = self.get_id(row, col, n, 0)
                    y = self.get_id(row-1, col, n, 2)
                    ufs.union(x, y)
                if col > 0:
                    # 合并当前格子的3和上边格子的1
                    x = self.get_id(row, col, n, 3)
                    y = self.get_id(row, col - 1, n, 1)
                    ufs.union(x, y)
                # 如果是/则合并当前格子的0,3、1,2；
                # 如果是\则合并当前格子的0,1、2,3；
                if g != "\\":
                    # 合并03
                    x = self.get_id(row, col, n, 0)
                    y = self.get_id(row, col, n, 3)
                    ufs.union(x, y)
                    # 合并12
                    x = self.get_id(row, col, n, 1)
                    y = self.get_id(row, col, n, 2)
                    ufs.union(x, y)
                if g != "/":
                    # 合并01
                    x = self.get_id(row, col, n, 0)
                    y = self.get_id(row, col, n, 1)
                    ufs.union(x, y)
                    # 合并23
                    x = self.get_id(row, col, n, 2)
                    y = self.get_id(row, col, n, 3)
                    ufs.union(x, y)
        return ufs.count

    def get_id(self, row, col, n, i):
        """
        获取到对应的数字
        :param n: 一行有多少
        :param row: 行
        :param col: 列
        :param i: id，0，1，2，3
        :return:
        """
        return (row * n + col) * 4 + i

    def run(self):
        grid = [
            " /",
            "/ "
        ]
        r = self.regionsBySlashes(grid)
        print(r)


s = Solution()
s.run()
