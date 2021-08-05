class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # 有环说明不安全
        n = len(graph)
        c = [0] * n  # 0为未搜索，1为搜索过，2为安全

        def foo(node):
            # 查找安全节点
            if c[node] > 0:
                # return c[node] == 2
                if c[node] == 1:
                    # 说明被搜索过,节点在环上,不安全
                    return False
                else:
                    return True
            c[node] = 1  # 标记为搜索过
            # 查找下一个节点
            for node_next in graph[node]:
                if not foo(node_next):
                    return False
            c[node] = 2  # 标记为安全节点
            return True

        r = list()
        for node in range(n):
            if foo(node):
                r.append(node)
        return r
