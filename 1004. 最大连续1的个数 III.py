class Solution:

    def longestOnes(self, A: list, K: int) -> int:
        start, end, count_0, count_1, n = 0, 0, 0, 0, len(A)
        r = 0
        for end in range(n):
            if A[end] == 1:
                count_1 += 1
            if A[end] == 0:
                count_0 += 1
            while count_0 > K:
                if A[start] == 1:
                    count_1 -= 1
                if A[start] == 0:
                    count_0 -= 1
                start += 1
            r = max(r, end - start + 1)
        return r

    def run(self):
        A = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
        K = 2
        r = self.longestOnes(A, K)
        print(r)


s = Solution()
s.run()
