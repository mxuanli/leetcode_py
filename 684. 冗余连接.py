class UnionFindSet:
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


class Solution:

    def findRedundantConnection(self, edges: list) -> list:
        ufs = UnionFindSet()
        r_list = list()
        r_list.append([])
        for edge in edges:
            x, y = edge
            xf, yf = ufs.find(x), ufs.find(y)
            if xf != yf:
                ufs.merge(x, y)
            else:
                r_list.append([x, y])
        return r_list[-1]

    def run(self):
        edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
        r = self.findRedundantConnection(edges)
        print(r)


s = Solution()
s.run()
