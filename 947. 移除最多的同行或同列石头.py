class UnionFindSet2:
    """
    并查集类
    """

    def __init__(self):
        self.father = dict()

    def add(self, x):
        # 添加节点
        if x not in self.father:
            self.father[x] = None

    def merge(self, x, y):
        # 合并节点
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            self.father[rx] = ry

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


class UnionFindSet:

    def __init__(self):
        self.father = dict()

    def find(self, x):
        root = x
        # 查找
        while self.father.get(root) is not None:
            root = self.father[root]
        # 压缩为两层
        while root != x:
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


class Solution:

    def removeStones(self, stones: list) -> int:
        if len(stones) == 1 or len(stones) == 0:
            return 0
        ufs = UnionFindSet()
        # x座标和y座标意义不一样，所以把y映射到其它区域，如（3, 3）座标的两个3是不一样的
        for x, y in stones:
            ufs.union(x, y + 15000)
        uf_set = set()
        for x, _ in stones:
            xv = ufs.find(x)
            uf_set.add(xv)
        return len(stones) - len(uf_set)

    def run(self):
        stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
        r = self.removeStones(stones)
        print(r)


s = Solution()
s.run()
