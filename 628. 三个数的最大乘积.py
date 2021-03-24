class Solution:
    def maximumProduct2(self, nums: list) -> int:
        nums.sort()
        r = max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
        return r

    def maximumProduct(self, nums: list) -> int:
        max1 = -1001
        max2 = -1002
        max3 = -1003
        min1 = 1005
        min2 = 1004
        for num in nums:
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num
        r = max(max1 * max2 * max3, min1 * min2 * max1)
        return r

    def run(self):
        nums = [-1, -2, -3]
        r = self.maximumProduct(nums)
        print(r)


s = Solution()
s.run()
