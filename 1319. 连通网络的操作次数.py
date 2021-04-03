class UnionFindSet:
    def __init__(self, n):
        self.father = dict()
        self.n = n

    def find(self, x):
        # 查找
        root = x
        while self.father.get(root) is not None:
            root = self.father[root]
        # 合并
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
            self.n -= 1



class Solution:

    def makeConnected(self, n: int, connections: list) -> int:
        len_c = len(connections)
        if n - 1 > len_c:
            return -1
        # 生成并查集，找出多余的边
        ufs = UnionFindSet(n)
        count = 0
        for connection in connections:
            x, y = connection
            ufs.union(x, y)
        len_u = len(ufs.father)
        return ufs.n - 1

    def run(self):
        n = 4
        connections = [[0, 1], [0, 2], [1, 2]]
        r = self.makeConnected(n, connections)
        print(r)


s = Solution()
s.run()
