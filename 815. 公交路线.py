class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        # 公交车可以到达的车站
        routes_dict = defaultdict(set)
        for i, route in enumerate(routes):
            for r in route:
                routes_dict[r].add(i)

        q = deque([(source, 0)])  # 搜索队列
        lines = set()  # 搜索过的路线
        stops = {source, }  # 搜索过的车站

        while q:
            stop, step = q.popleft()
            if stop == target:
                return step
            line = routes_dict[stop]  # 车站能到的路线集合
            lines_diff = line - lines  # 尚未搜索过的路线
            for l in lines_diff:
                stops_diff = set(routes[l]) - stops  # 尚未搜索过的车站
                for stop in stops_diff:
                    q.append((stop, step + 1))
                lines.add(l)
                stops.add(stop)
        return -1
