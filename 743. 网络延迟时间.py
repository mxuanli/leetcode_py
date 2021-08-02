from collections import defaultdict


class Solution:
    # Dijkstra 最短路径算法
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        max_w = n * 100 + 1
        dis_w = [max_w for _ in range(n + 1)]
        bool_list = [False for _ in range(n + 1)]
        dis_w[k] = 0
        time_dict = defaultdict(lambda: defaultdict(int))
        for time in times:
            time_dict[time[0]][time[1]] = time[2]
        while True:
            # 找到没被添加过的最小的值
            cur, min_w = -1, max_w  # 最小值下标，最小值
            for i, b in enumerate(dis_w):
                if not bool_list[i] and b < min_w:
                    cur, min_w = i, b
            # 没找到说明被搜索完了，返回
            if cur == -1:
                break
            # 更新数据
            bool_list[cur] = True
            # 计算能达到的下一个节点的最小值
            for vi, wi in time_dict[cur].items():
                dis_w[vi] = min(dis_w[vi], min_w + wi)
        r = max(dis_w[1:])
        if r == max_w:
            return -1
        else:
            return r
