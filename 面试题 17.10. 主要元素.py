class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 摩尔投票法
        major = 0
        count = 0
        for num in nums:
            if count == 0:
                major = num
            if num == major:
                count += 1
            else:
                count -= 1
        if nums.count(major) > len(nums) // 2:
            return major
        return -1
