class UnionFindSet:

    def __init__(self, n):
        self.parent = dict()
        self.count = n

    def find(self, x):
        # 查找
        root = x
        while self.parent.get(root) is not None:
            root = self.parent[root]
        # 压缩
        while root != x:
            father_root = self.parent[x]
            self.parent[x] = root
            x = father_root
        return root

    def union(self, x, y):
        # 压缩
        xf = self.find(x)
        yf = self.find(y)
        if xf != yf:
            self.parent[xf] = yf
            self.count -= 1

class Solution:

    def numSimilarGroups(self, strs: list) -> int:
        n = len(strs)
        ufs = UnionFindSet(n)
        for i in range(n):
            for j in range(i + 1, n):
                str_i = strs[i]
                str_j = strs[j]
                if self.is_similar(str_i, str_j):
                    ufs.union(i, j)
        return ufs.count

    def is_similar(self, A, B):
        # 是否相似
        if A == B:
            return True
        count = 0
        for i in range(len(A)):
            ai, bi = A[i], B[i]
            if ai != bi:
                count += 1
        return count == 2

    def run(self):
        strs = ["abc","abc"]
        r = self.numSimilarGroups(strs)
        print(r)


s = Solution()
s.run()
