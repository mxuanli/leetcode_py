class UnionFindSet:

    def __init__(self):
        self.father = dict()

    def find(self, x):
        # 查找
        root = x
        while self.father.get(root) is not None:
            root = self.father[root]
        # 压缩路径
        while x != root:
            father_code = self.father[x]
            self.father[x] = root
            x = father_code
        return root

    def union(self, x, y):
        # 压缩
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

    def minimumEffortPath(self, heights: list) -> int:
        n = len(heights)  # 高
        m = len(heights[0])  # 宽
        tmp_list = list()
        # 计算相邻格子之间的高度差绝对值
        for i in range(n):
            for j in range(m):
                this_id = i * m + j
                if i > 0:
                    up_id = this_id - m
                    tmp = (up_id, this_id, abs(heights[i][j] - heights[i - 1][j]))
                    tmp_list.append(tmp)
                if j > 0:
                    left_id = this_id - 1
                    tmp = (left_id, this_id, abs(heights[i][j] - heights[i][j - 1]))
                    tmp_list.append(tmp)
        # 排序
        tmp_list.sort(key=lambda x: x[2])
        # 连通性
        start, end = 0, n * m - 1
        ufs = UnionFindSet()
        for tmp in tmp_list:
            x, y, r = tmp
            ufs.union(x, y)
            if ufs.is_conn(start, end):
                return r
        return 0

    def run(self):
        heights = [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]
        r = self.minimumEffortPath(heights)
        print(r)


s = Solution()
s.run()
