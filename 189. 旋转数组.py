class Solution:

    def rotate2(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]
        print(nums)

    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_n = len(nums)
        nums_k = nums[:len_n - k]
        del nums[:len_n - k]
        nums += nums_k
        print(nums)

    def run(self):
        nums = [1, 2]
        k = 3
        self.rotate2(nums, k)


s = Solution()
s.run()
