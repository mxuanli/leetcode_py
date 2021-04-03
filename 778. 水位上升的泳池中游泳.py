class UnionFindSet:
    def __init__(self):
        self.parent = dict()

    def find(self, x):
        # 查找
        root = x
        while self.parent.get(root) is not None:
            root = self.parent[root]
        # 压缩
        while root != x:
            father_code = self.parent[x]
            self.parent[x] = root
            x = father_code
        return root

    def union(self, x, y):
        # 压缩
        xf = self.find(x)
        yf = self.find(y)
        if xf != yf:
            self.parent[xf] = yf

    def is_conn(self, x, y):
        # 判断连接
        xf = self.find(x)
        yf = self.find(y)
        if xf != yf:
            return False
        return True


class Solution:

    def swimInWater(self, grid: list) -> int:
        tmp_list = list()
        n = len(grid)  # 高
        m = len(grid[0])  # 宽
        for i in range(n):  # 高
            for j in range(m):  # 宽
                x = i * m + j
                if i < n - 1:
                    y = x + m
                    tmp = (x, y, max(grid[i][j], grid[i + 1][j]))
                    tmp_list.append(tmp)
                if j < m - 1:
                    y = x + 1
                    tmp = (x, y, max(grid[i][j], grid[i][j + 1]))
                    tmp_list.append(tmp)
        tmp_list.sort(key=lambda x: x[2])
        ufs = UnionFindSet()
        start, end = 0, n * m - 1
        for tmp in tmp_list:
            x, y, v = tmp[0], tmp[1], tmp[2]
            ufs.union(x, y)
            if ufs.is_conn(start, end):
                return v
        return -1

    def run(self):
        grid = [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
        r = self.swimInWater(grid)
        print(r)


s = Solution()
s.run()
