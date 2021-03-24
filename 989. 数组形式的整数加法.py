class Solution:

    def addToArrayForm(self, A: list, K: int) -> list:
        x = 0
        for i in A:
            x *= 10
            x += i
        r = x + K
        r_list = list()
        if r == 0:
            r_list = [0]
        while r != 0:
            k = r % 10
            r = r // 10
            r_list.append(k)
        return r_list[::-1]

    def run(self):
        A = [1, 2, 0, 0]
        K = 34
        r = self.addToArrayForm(A, K)
        print(r)


s = Solution()
s.run()
