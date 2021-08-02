from collections import defaultdict


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dict_mat = defaultdict(list)
        for i, m in enumerate(mat):
            dict_mat[sum(m)].append(i)
        num = 0
        r = list()
        for i in sorted(dict_mat):

            for j in dict_mat[i]:
                if num >= k:
                    break
                r.append(j)
                num += 1
        return r
