class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        prefixsum = [0]
        for c in candiesCount:
            prefixsum.append(c + prefixsum[-1])
        print(prefixsum)
        answer = [False for _ in range(len(queries))]
        for i, querie in enumerate(queries):
            favoriteType = querie[0]
            favoriteDay = querie[1]
            dailyCap = querie[2]
            min_ = favoriteDay  # 今天之前最少吃的数量
            max_ = (favoriteDay + 1) * dailyCap - 1  # 带上今天最多吃的数量
            low = prefixsum[favoriteType]  # 糖果的最小编号
            high = prefixsum[favoriteType + 1] - 1  # 糖果的最大编号
            # 如果糖果的最小编号大于最多吃的数量，或者最少吃的数量大于糖果的最大编号，则为False，反之为True
            if not (max_ < low or high < min_):
                answer[i] = True
        return answer

