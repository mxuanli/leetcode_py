class Solution:

    def matrixReshape2(self, nums: list, r: int, c: int) -> list:
        nums2 = list()
        for num in nums:
            nums2 += num
        n = len(nums2)
        if n // r != c:
            return nums
        last_i = 0
        res = list()
        for i in range(c, n + 1, c):
            res.append(nums2[last_i: i])
            last_i = i
        return res

    def matrixReshape(self, nums: list, r: int, c: int) -> list:
        m, n = len(nums), len(nums[0])
        len_n = n * m
        if len_n // r != c:
            return nums
        res = [[0] * c for i in range(r)]
        for i in range(len_n):
            res[i // c][i % c] = nums[i // n][i % n]
        return res

    def run(self):
        nums = [[1, 2],
                [3, 4]]
        r = 1
        c = 4
        r = self.matrixReshape(nums, r, c)
        print(r)


s = Solution()
s.run()

