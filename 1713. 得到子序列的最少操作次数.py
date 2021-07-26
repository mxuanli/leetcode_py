class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        pos = dict()
        # key为值，v为下标
        for v, k in enumerate(target):
            pos[k] = v
        r = list()
        # 求最长最长递增子序列
        for num in arr:
            if num in pos:
                v = pos.get(num)
                i = bisect.bisect_left(r, v)
                if i < len(r):
                    r[i] = v
                else:
                    r.append(v)
        return len(target) - len(r)
