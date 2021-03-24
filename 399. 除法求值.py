from collections import defaultdict


class Solution:

    def calcEquation(self, equations: list, values: list, queries: list) -> list:
        dd = defaultdict(dict)
        for (x, y), v in zip(equations, values):
            dd[x][y] = v
            dd[y][x] = 1 / v
        r = list()
        for start, end in queries:
            way = set()
            qr = self.dfs(start, end, way, dd)
            r.append(qr)
        return r

    def dfs(self, start, end, way, dd):
        way.add(start)
        if start not in dd:
            return -1
        if start == end:
            return 1
        for z in dd[start]:
            if z == end:
                return dd[start][z]
            if z not in way:
                way.add(z)
                # 寻找路径
                v = self.dfs(z, end, way, dd)
                if v != -1:
                    return v * dd[start][z]
                else:
                    pass
        # 找不到就返回-1
        return -1

    def run(self):
        equations = [["x1", "x2"], ["x2", "x3"], ["x3", "x4"], ["x4", "x5"]]
        values = [3.0, 4.0, 5.0, 6.0]
        queries = [["x1", "x5"], ["x5", "x2"], ["x2", "x4"], ["x2", "x2"], ["x2", "x9"], ["x9", "x9"]]
        r = self.calcEquation(equations, values, queries)
        print(r)


s = Solution()
s.run()
