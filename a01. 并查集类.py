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
