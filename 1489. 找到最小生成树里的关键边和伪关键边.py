class UnionFindSet:
    """
    并查集类
    """

    def __init__(self):
        self.father = dict()

    def find(self, x):
        # 查找
        root = x
        while self.father.get(root) is not None:
            root = self.father[root]
        # 合并
        while root != x:
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

    def is_conn(self, x, y):
        # 判断连接
        xf = self.find(x)
        yf = self.find(y)
        if xf != yf:
            return False
        return True


class Solution:

    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: list) -> list:
        # 添加边的下标
        edges = [edge + [i] for i, edge in enumerate(edges)]
        # 排序
        edges_sort_list = sorted(edges, key=lambda x: x[-2])
        ufs = UnionFindSet()
        num = 1
        total = 0
        # 最小生成树
        for edge in edges_sort_list:
            w = edge[2]  # 边长
            x = edge[0]
            y = edge[1]
            is_conn = ufs.is_conn(x, y)
            if not is_conn:
                ufs.union(x, y)
                total += w
                n += 1
                if num == n:
                    break
        r1 = list()  # 关键边
        r2 = list()  # 伪关键边
        # 遍历
        for i, this_edge in enumerate(edges_sort_list):
            edges_tmp = edges_sort_list[:i] + edges_sort_list[i + 1:]
            this_x = this_edge[0]
            this_y = this_edge[1]
            this_w = this_edge[2]
            this_i = this_edge[3]
            # 先连接当前边之后的总权值
            ufs = UnionFindSet()
            total0 = this_w
            ufs.union(this_x, this_y)
            for edge in edges_tmp:
                x = edge[0]
                y = edge[1]
                w = edge[2]
                if not ufs.is_conn(x, y):
                    ufs.union(x, y)
                    total0 += w
            # 去掉当前边的权值
            ufs = UnionFindSet()
            total1 = 0
            for edge in edges_tmp:
                x = edge[0]
                y = edge[1]
                w = edge[2]
                if not ufs.is_conn(x, y):
                    ufs.union(x, y)
                    total1 += w
            # 和total比较，如果total和total0相等，说明是有效边
            if total == total0:
                # 如果total0和total1不相等，则是关键边
                if total0 != total1:
                    r1.append(this_i)
                # 否则为伪关键边
                else:
                    r2.append(this_i)
        r = [r1, r2]
        return r

    def run(self):
        n = 5
        edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]]
        r = self.findCriticalAndPseudoCriticalEdges(n, edges)
        print(r)


s = Solution()
s.run()
