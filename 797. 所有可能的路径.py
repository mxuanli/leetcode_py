class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        n_1 = n - 1
        r = list()
        q = collections.deque([(0, [0])])
        while q:
            g0, g1 = q.popleft()
            if g0 == n_1:
                r.append(list(g1))
                continue
            for t in graph[g0]:
                next_ = (t, g1 + [t])
                q.append(next_)
        return r


class Solution1:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        r = list()
        q = collections.deque([([0])])
        while q:
            g = q.popleft()
            g1, g0 = g, g[-1]
            if g0 == n - 1:
                r.append(g1)
                continue
            for t in graph[g0]:
                q.append(g1 + [t])
        return r
