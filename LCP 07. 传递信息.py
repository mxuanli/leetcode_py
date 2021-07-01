class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        relation_hash = defaultdict(list)
        for r in relation:
            relation_hash[r[0]].append(r[1])

        q = deque([0])
        step = 0
        r = 0
        while q and step < k:
            # 所有本步可以到达的位置
            size = len(q)
            for i in range(size):
                start = q.popleft()  # 当前位置
                # 可到达位置
                end_list = relation_hash[start]
                for end in end_list:
                    q.append(end)
            step += 1  # 步数 + 1
        if step == k:
            while q:
                if q.popleft() == n - 1:
                    r += 1
        return r
