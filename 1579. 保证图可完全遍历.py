class UnionFindSet:

    def __init__(self, n):
        self.father = dict()
        self.count = n

    def find(self, x):
        # 查找
        root = x
        while self.father.get(root) is not None:
            root = self.father[root]
        # 压缩
        while x != root:
            father_code = self.father[x]
            self.father[x] = root
            x = father_code
        return root

    def union(self, x, y):
        # 合并
        xf = self.find(x)
        yf = self.find(y)
        if xf != yf:
            self.father[xf] = yf
            self.count -= 1

    def is_conn(self, x, y):
        # 判断连接
        xf = self.find(x)
        yf = self.find(y)
        if xf == yf:
            return True
        return False


class Solution:

    def maxNumEdgesToRemove2(self, n: int, edges: list) -> int:
        edges_1 = list()
        edges_2 = list()
        edges_3 = list()
        for edge in edges:
            t = edge[0]
            if t == 1:
                edges_1.append(edge)
            elif t == 2:
                edges_2.append(edge)
            elif t == 3:
                edges_3.append(edge)
        r = 0
        ufs_a = UnionFindSet(n)
        ufs_b = UnionFindSet(n)
        # 公共边
        for edge in edges_3:
            _, x, y = edge
            a = ufs_a.is_conn(x, y)
            b = ufs_b.is_conn(x, y)
            if a and b:
                r += 1
            if not a:
                ufs_a.union(x, y)
            if not b:
                ufs_b.union(x, y)
        # a边
        for edge in edges_1:
            _, x, y = edge
            if ufs_a.is_conn(x, y):
                r += 1
            else:
                ufs_a.union(x, y)
        # b边
        for edge in edges_2:
            _, x, y = edge
            if ufs_b.is_conn(x, y):
                r += 1
            else:
                ufs_b.union(x, y)
        if ufs_a.count > 1 or ufs_b.count > 1:
            return -1
        return r

    def maxNumEdgesToRemove(self, n: int, edges: list) -> int:
        r = 0
        ufs_a = UnionFindSet(n)
        ufs_b = UnionFindSet(n)
        for edge in edges:
            t, x, y = edge
            # 公共边
            if t == 3:
                a = ufs_a.is_conn(x, y)
                b = ufs_b.is_conn(x, y)
                if a and b:
                    r += 1
                if not a:
                    ufs_a.union(x, y)
                if not b:
                    ufs_b.union(x, y)
        for edge in edges:
            t, x, y = edge
            # a边
            if t == 1:
                if ufs_a.is_conn(x, y):
                    r += 1
                else:
                    ufs_a.union(x, y)
            # b边
            elif t == 2:
                if ufs_b.is_conn(x, y):
                    r += 1
                else:
                    ufs_b.union(x, y)
        if ufs_a.count > 1 or ufs_b.count > 1:
            return -1
        return r

    def run(self):
        n = 2
        edges = [[1, 1, 2], [2, 1, 2], [3, 1, 2]]
        r = self.maxNumEdgesToRemove(n, edges)
        print(r)


s = Solution()
s.run()
