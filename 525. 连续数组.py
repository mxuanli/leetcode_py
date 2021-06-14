class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        pre = dict()
        pre[0] = -1
        tmp = 0
        r = 0
        for i, num in enumerate(nums):
            if num != 0:
                tmp += num
            else:
                tmp -= 1
            if tmp in pre:
                diff = i - pre[tmp]
                if diff >= 2:
                    r = max(diff, r)
            else:
                pre[tmp] = i
        return r
