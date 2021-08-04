class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        r = 0
        for i in range(n):
            for j in range(i + 1, n):
                start, end = j + 1, n - 1
                k = j
                while start <= end:
                    mid = start + (end - start) // 2
                    if nums[mid] < nums[i] + nums[j]:
                        k = mid
                        start = mid + 1
                    else:
                        end = mid - 1
                r += k - j
        return r
