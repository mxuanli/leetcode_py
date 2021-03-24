class UnionSetFind:

    def __init__(self):
        self.father = dict()

    def find(self, x):
        # 查找根节点
        root = x
        # 查找
        while self.father.get(root) is not None:
            root = self.father[root]
        # 压缩
        while x != root:
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

    def is_connected(self, x, y):
        # 判断是否相连
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return True
        return False


class Solution:

    def minCostConnectPoints(self, points: list) -> int:
        usf = UnionSetFind()
        manhattan_nums_list = list()
        n = len(points)
        # 计算所有边长
        for i in range(n):
            for j in range(i + 1, n):
                x = points[i]
                y = points[j]
                manhattan_nums_list.append([self.manhattan(x, y), i, j])
        manhattan_nums_list.sort()
        r = 0
        num = 1
        print(manhattan_nums_list)
        # 计算最短路径
        for manhattan_nums in manhattan_nums_list:
            manhattan_num = manhattan_nums[0]
            i = manhattan_nums[1]
            j = manhattan_nums[2]
            is_connected = usf.is_connected(i, j)
            if not is_connected:
                usf.union(i, j)
                r += manhattan_num
                num += 1
                if num == n:
                    break
        return r

    def manhattan(self, x: list, y: list):
        # 计算曼哈顿距离
        xv = abs(x[0] - y[0])
        yv = abs(x[1] - y[1])
        r = xv + yv
        return r

    def run(self):
        points = [[11, -6], [9, -19], [16, -13], [4, -9], [20, 4], [20, 7], [-9, 18], [10, -15], [-15, 3], [6, 6]]
        r = self.minCostConnectPoints(points)
        print(r)


s = Solution()
s.run()
