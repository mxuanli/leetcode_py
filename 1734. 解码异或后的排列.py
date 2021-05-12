class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        r = list()
        n = len(encoded)
        if n < 2:
            return r
        # perm是是前 n 个正整数的排列，perm值比encoded多一个值
        # 求perm（ABCDE）所有元素异或的值
        p2_n = 0
        for i in range(1, n + 2):
            p2_n ^= i
        p1_n = 0
        # 求奇数位的值，encoded所有奇数位的值等于perm除去第一个元素之外的异或值（perm的ABCD）
        for i in range(1, n, 2):
            p1_n ^= encoded[i]
        r.append(p2_n ^ p1_n)
        for e in encoded:
            r.append(r[-1] ^ e)
        return r
