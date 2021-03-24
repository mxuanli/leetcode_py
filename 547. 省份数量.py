class UnionFindSet:
    """
    并查集类
    """
    def __init__(self):
        self.father = dict()
        self.nums = 0

    def add(self, x):
        # 添加节点
        if x not in self.father:
            self.nums += 1
            self.father[x] = None

    def merge(self, x, y):
        # 合并节点
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            self.nums -= 1
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
        while self.father[root] is not None:
            root = self.father[root]
        # 压缩
        while x != root:
            father_code = self.father[x]
            self.father[x] = root
            x = father_code
        return root


class Solution:

    def findCircleNum(self, isConnected: list):
        ufs = UnionFindSet()
        for i in range(len(isConnected)):
            ufs.add(i)
            for j in range(i):
                if isConnected[i][j] == 1:
                    ufs.add(j)
                    ufs.merge(i, j)
        return ufs.nums

    def run(self):
        isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
        r = self.findCircleNum(isConnected)
        print(r)


s = Solution()
s.run()

