
class Solution:

    def minPatches(self, nums: list, n: int) -> int:
        r = 0
        x, index = 1, 0
        len_nums = len(nums)
        while x <= n:
            # 区间[1,x−1]的数字已经都被覆盖，如果x大于nums[index]才需要添加数
            if index < len_nums and nums[index] <= x:
                x += nums[index]
                index += 1
            # 添加数字进去
            else:
                x *= 2
                r += 1
        return r

    def run(self):
        nums = [1, 5, 10]
        n = 20
        r = self.minPatches(nums, n)
        print(r)


s = Solution()
s.run()
