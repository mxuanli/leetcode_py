from sortedcontainers import SortedList


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # 如果最高点发生变化就保存下来
        r = list()
        tmp = list()
        for left, right, height in buildings:
            tmp.append((left, -height))
            tmp.append((right, height))
        tmp.sort()
        lives = SortedList([0])
        prev = 0
        for x, h in tmp:
            if h < 0:
                lives.add(h)
            else:
                lives.remove(-h)
            max_len = -lives[0]
            if max_len != prev:  # 最高点发生了变化
                r.append([x, max_len])
            prev = max_len
        return r
