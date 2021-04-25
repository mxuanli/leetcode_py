class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        start, end = 0, 0
        diff_sum = 0
        r = 1
        for end in range(n):
            diff_sum += (nums[end] - nums[end - 1]) * (end - start)  # 计算窗口内的差值和，每新增一个元素，差值和就会新增（元素数）*（新增元素 - 上一个元素）
            if diff_sum <= k:
                r = max(r, end - start + 1)
            while diff_sum > k:
                diff_sum -= nums[end] - nums[start]
                start += 1
        return r
