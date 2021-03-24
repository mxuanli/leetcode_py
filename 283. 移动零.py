class Solution:

    def moveZeroes2(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                zero_count += 1
                del nums[i]
        for i in range(zero_count):
            nums.append(0)
        print(nums)

    def moveZeroes3(self, nums: list) -> None:
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
        print(nums)

    def moveZeroes(self, nums: list) -> None:
        fast, slow = 0, 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1
        print(nums)

    def run(self):
        nums = [0, 1, 0, 3, 12]
        self.moveZeroes(nums)


s = Solution()
s.run()
