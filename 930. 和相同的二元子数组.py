from collections import defaultdict


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dict_nums = defaultdict(int)
        sum_nums = 0
        r = 0
        for num in nums:
            dict_nums[sum_nums] += 1  # num的前缀和sum_nums，在hash里数量+1
            sum_nums += num  # 求num+1的前缀和
            r += dict_nums[sum_nums - goal]  # 计算前缀和为sum_nums - goal的数量，中间的这段子数组就是符合要求的子数组
        return r


class Solution1:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        left1, left2 = 0, 0
        sum1, sum2 = 0, 0
        r = 0
        for right, num in enumerate(nums):
            sum1 += num
            while left1 <= right and sum1 > goal:
                sum1 -= nums[left1]
                left1 += 1
            sum2 += num
            while left2 <= right and sum2 >= goal:
                sum2 -= nums[left2]
                left2 += 1
            r += left2 - left1
        return r
