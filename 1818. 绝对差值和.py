import bisect


class Solution:
    def minAbsoluteSumDiff(self, nums1: list, nums2: list) -> int:
        nums3 = sorted(nums1)
        sum_diff = 0
        n = len(nums1)
        max_diff = 0
        for i, num in enumerate(nums2):
            diff = abs(nums1[i] - num)  # 绝对值差值
            sum_diff += diff
            j = bisect.bisect_right(nums3, num)  # 在nums1中找到和num差值最小的
            if j < n:
                max_diff = max(max_diff, diff - (nums3[j] - num))  # 假如nums1中的值比目标值大
            if j > 0:
                max_diff = max(max_diff, diff - (num - nums3[j - 1]))  # # 假如nums1中的值比目标值小
        return (sum_diff - max_diff) % (10 ** 9 + 7)


s = Solution()
r = s.minAbsoluteSumDiff([1, 10, 4, 4, 2, 7], [9, 3, 5, 1, 7, 4])
print(r)
