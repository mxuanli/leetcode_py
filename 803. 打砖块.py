class UnionFindSet:
    """
    并查集类
    """

    def __init__(self):
        self.father = dict()
        self.size_of_set = dict()  # 根节点连通的砖块数量

    def add(self, x):
        # 添加节点
        if x not in self.father:
            self.father[x] = None
            self.size_of_set[x] = 1

    def get_set_size(self, x):
        # 获取连通的砖块数量
        return self.size_of_set.get(self.find(x), 0)

    def merge(self, x, y):
        # 合并节点
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            self.father[rx] = ry
            # 合并连接数量
            self.size_of_set[ry] += self.size_of_set[rx]
            del self.size_of_set[rx]

    def is_connected(self, x, y):
        # 判断是否相连
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return True
        return False

    def find(self, x):
        root = x
        # 直到查到找祖先节点，即父节点为空的节点
        while self.father.get(root) is not None:
            root = self.father[root]
        # 压缩
        while x != root:
            father_code = self.father[x]
            self.father[x] = root
            x = father_code
        return root


class Solution:

    def __init__(self):
        self.ceiling = (-1, -1)  # 天花板
        self.up_down_left_right = ((0, -1), (0, 1), (-1, 0), (1, 0))  # 上下左右

    def initialize(self, grid, hits, m, n, ufs: UnionFindSet):
        # 添加一个天花板
        ufs.add(self.ceiling)
        # 敲掉所有砖
        for x, y in hits:
            grid[x][y] -= 1
        # 添加所有砖块进去
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ufs.add((i, j))
        # 链接，合并砖块（和上下左右合并）
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.merge_up_down_left_right(i, j, grid, m, n, ufs)

        # 合并天花板（x坐标为0的才能合并）
        for j in range(n):
            if grid[0][j] == 1:
                ufs.merge((0, j), self.ceiling)

    def merge_up_down_left_right(self, x, y, grid, m, n, ufs: UnionFindSet):
        # 合并上下左右
        for mx, my in self.up_down_left_right:
            nx, ny = x + mx, y + my
            # 校验是否可以合并
            if not self.is_valid(nx, ny, grid, m, n):
                continue
            # 合并
            ufs.merge((x, y), (nx, ny))

    def is_valid(self, x, y, grid, m, n):
        # 判断目标是否出界，且是否是砖块
        if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
            return True
        else:
            return False

    def hitBricks(self, grid: list, hits: list) -> list:
        ufs = UnionFindSet()
        m, n = len(grid), len(grid[0])
        res = [0] * len(hits)  # 初始化结果列表，方便后边填值
        # 初始化数据，敲砖，合并等
        self.initialize(grid, hits, m, n, ufs)
        # 逆序填补砖块
        for i in range(len(hits) - 1, -1, -1):
            x, y = hits[i][0], hits[i][1]

            # 填补砖块
            grid[x][y] += 1

            # 如果原本就不是砖就跳过
            if grid[x][y] != 1:
                continue

            # 没填补之前的天花板连接数量
            before_add = ufs.get_set_size(self.ceiling)

            # 填补砖块，并合并
            ufs.add((x, y))
            self.merge_up_down_left_right(x, y, grid, m, n, ufs)

            # 连接天花板
            if x == 0:
                ufs.merge((x, y), self.ceiling)

            # 计算填补之后的连接天花板的数量
            if ufs.is_connected((x, y), self.ceiling):
                after_add = ufs.get_set_size(self.ceiling)
                # 计算添加了砖块之后的新增数量
                res[i] = after_add - before_add - 1
        return res

    def run(self):
        grid = [[1, 0, 0, 0], [1, 1, 1, 0]]
        hits = [[1, 0]]
        r = self.hitBricks(grid, hits)
        print(r)


s = Solution()
s.run()
