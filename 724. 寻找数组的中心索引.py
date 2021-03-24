class Solution:

    def pivotIndex1(self, nums: list) -> int:
        n = len(nums)
        for i in range(n):
            num1 = sum(nums[:i])
            num2 = sum(nums[i + 1:])
            if num1 == num2:
                return i
        return -1

    def pivotIndex(self, nums: list) -> int:
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i + 1:]):
                return i
        return -1

    def run(self):
        nums = [-1, -1, -1, -1, -1, -1]
        r = self.pivotIndex(nums)
        print(r)


s = Solution()
s.run()
