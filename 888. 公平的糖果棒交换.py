class Solution:

    def fairCandySwap(self, A: list, B: list) -> list:
        age = (sum(A) - sum(B)) // 2  # 差值除以2
        for i in B:
            j = i + age
            if j in A:
                return [j, i]
        return []


    def run(self):
        A = [1, 1]
        B = [2, 2]
        r = self.fairCandySwap(A, B)
        print(r)


s = Solution()
s.run()

