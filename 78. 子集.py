
class Solution:

    def subsets(self, nums: list) -> list:
        res = [[]]
        for i in nums:
            res = res + [[i] + r for r in res]
        return res

    def run(self):
        nums = [1, 2, 3]
        r = self.subsets2(nums)
        print(r)

    def subsets2(self, nums: list) -> list:
        res = []
        l = len(nums)

        def foo(i, tmp):
            res.append(tmp)
            for j in range(i, l):
                foo(j+1, tmp + [nums[j]])

        foo(0, [])
        return res


s = Solution()
s.run()
