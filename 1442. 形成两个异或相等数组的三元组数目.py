class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        tmp = list()
        tmp += [0]
        for i in arr:
            tmp.append(tmp[-1] ^ i)
        n = len(arr)
        r = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j, n):
                    if tmp[i] == tmp[k + 1]:
                        r += 1
        return r


class Solution1:
    def countTriplets(self, arr: List[int]) -> int:
        tmp = list()
        tmp += [0]
        for i in arr:
            tmp.append(tmp[-1] ^ i)
        n = len(arr)
        r = 0
        for i in range(n):
            for k in range(i + 1, n):
                if tmp[i] == tmp[k + 1]:  # 当tmp[i] == tmp[k + 1]成立时，任意j都成立，这时候三元数组数是k - i
                    r += k - i
        return r
