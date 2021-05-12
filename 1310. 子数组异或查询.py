class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # a^b^c^d^e=xor，那么d^e=(a^b^c)^xor
        xors = [0]
        for a in arr:
            xors.append(xors[-1] ^ a)
        r = list()
        for i, j in queries:
            r.append(xors[i] ^ xors[j + 1])
        return r
