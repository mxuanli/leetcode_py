class Solution1:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        q = deque()
        pre = set()
        for i in range(n):
            status = 1 << i
            q.append((i, status, 0))  # (i, set, step)表示(节点, 到达此节点时每一个节点是否经过（为1）, 到达此节点的步数)
            pre.add((i, status))  # (i, set)表示(节点, 到达此节点时每一个节点的状态)
        r = 0
        goal = tuple([1] * n)
        while q:
            i, status, step = q.popleft()  # 节点，状态，步数
            # 所有节点都经过
            if status == (1 << n) - 1:
                r = step
                break
            # 能到达的节点
            for next_i in graph[i]:
                # 下一个节点的状态，把下一个节点改成已经过（改成1）
                next_status = status | (1 << next_i)
                # 如果状态没被搜索过，则添加到队列，防止重复搜索
                if (next_i, next_status) not in pre:
                    q.append((next_i, next_status, step + 1))
                    pre.add((next_i, next_status))
        return r


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        q = deque()
        pre = set()
        for i in range(n):
            # status = [0] * n
            # status[i] = 1  # 以每个节点为起点都进行一次搜索
            # status = tuple(status)
            status = 1 << i
            q.append((i, status, 0))  # (i, set, step)表示(节点, 到达此节点时每一个节点是否经过（为1）, 到达此节点的步数)
            pre.add((i, status))  # (i, set)表示(节点, 到达此节点时每一个节点的状态)
        r = 0
        while q:
            i, status, step = q.popleft()  # 节点，状态，步数
            # 所有节点都经过
            # if status == goal:
            if status == (1 << n) - 1:
                r = step
                break
            # 能到达的节点
            for next_i in graph[i]:
                # 下一个节点的状态，把下一个节点改成已经过（改成1）
                # next_status = list(status)
                # next_status[next_i] = 1
                # next_status = tuple(next_status)
                next_status = status | (1 << next_i)
                # 如果状态没被搜索过，则添加到队列，防止重复搜索
                if (next_i, next_status) not in pre:
                    q.append((next_i, next_status, step + 1))
                    pre.add((next_i, next_status))
        return r
