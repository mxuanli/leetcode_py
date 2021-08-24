class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Dijkstra算法
        end_set = set()
        tmp = defaultdict(lambda: defaultdict(int))
        for flight in flights:
            end_set.add(flight[1])
            tmp[flight[0]][flight[1]] = flight[2]
        # 如果目的地没有终点，就排除
        if dst not in end_set:
            return -1
        import queue
        q = queue.PriorityQueue()
        q.put((0, src, k))  # 价格，位置，步数
        while not q.empty():
            cos, f, k = q.get()
            if f == dst:
                return cos
            if k >= 0:
                # 到达位置，价格
                for key, value in tmp[f].items():
                    q.put((cos + value, key, k - 1))
        return -1
