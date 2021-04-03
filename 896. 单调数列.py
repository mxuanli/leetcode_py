class Solution:
    def isMonotonic1(self, A: list) -> bool:
        if A == sorted(A) or A == sorted(A, reverse=True):
            return True
        return False

    def isMonotonic(self, A: list) -> bool:
        flag = None
        for i in range(1, len(A)):
            if flag == None:
                if A[i] > A[i - 1]:
                    flag = True
                elif A[i] < A[i - 1]:
                    flag = False
            if flag:
                if A[i] < A[i - 1]:
                    return False
            else:
                if A[i] > A[i - 1]:
                    return False
        return True

    def run(self):
        A = [1, 1, 2]
        r = self.isMonotonic(A)
        print(r)


s = Solution()
s.run()
