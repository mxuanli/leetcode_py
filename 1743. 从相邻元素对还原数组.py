from collections import defaultdict


class Solution:
    def restoreArray(self, adjacentPairs: list) -> list:
        # 统计数量，找到开头
        dict_adj = defaultdict(set)
        for adj in adjacentPairs:
            a, b = adj
            dict_adj[a].add(b)
            dict_adj[b].add(a)
        start = adjacentPairs[0][0]
        for k, v in dict_adj.items():
            if len(v) == 1:
                start = k
        # 组合列表
        r = [start]
        adj_set = {start}
        n = len(dict_adj)
        adj = start
        for i in range(n - 1):
            # 没有被添加进去的
            diff_adj = dict_adj[adj] - adj_set
            adj = diff_adj.pop()
            adj_set.add(adj)
            r.append(adj)
        return r


adjacentPairs = [[2, 1], [3, 4], [3, 2]]
s = Solution()
r = s.restoreArray(adjacentPairs)
print(r)
