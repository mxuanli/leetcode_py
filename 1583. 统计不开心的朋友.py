class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        pre_dict = defaultdict(list)
        # 转换成pre_dict[朋友x] = [亲近程度列表] 的形式
        for i, pre in enumerate(preferences):
            pre_dict[i] = pre
        # 转化成pairs_dict[朋友x] = [朋友y]的形式
        pairs_dict = defaultdict(int)
        for x, y in pairs:
            pairs_dict[x] = y
            pairs_dict[y] = x
        r = 0
        # 遍历朋友
        for x in range(n):
            y = pairs_dict[x]  # 找到y
            # 找到对于x来说比y亲进度高的人u
            i = pre_dict[x].index(y)
            for u in pre_dict[x][:i]:
                # 找到v
                v = pairs_dict[u]
                if pre_dict[u].index(x) < pre_dict[u].index(v):
                    r += 1
                    break
        return r
