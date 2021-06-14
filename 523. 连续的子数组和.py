class Solution:
    def checkSubarraySum(self, nums: list, k: int) -> bool:
        if len(nums) < 2:
            return False
        tmp = 0
        remainder_dict = dict()
        remainder_dict[0] = -1
        for i, num in enumerate(nums):
            tmp = (tmp + num) % k
            print(tmp)
            if tmp in remainder_dict:
                if i - remainder_dict[tmp] >= 2:
                    return True
            else:
                remainder_dict[tmp] = i
        return False


nums = [23, 2, 4, 6, 7]
k = 6
s = Solution()
r = s.checkSubarraySum(nums, k)
