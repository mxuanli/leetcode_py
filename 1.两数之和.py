nums = [2, 7, 11, 15]
target = 9


# nums[0] + nums[1] = 2 + 7 = 9

class Solution:
    """
    设置dict_a记录元素索引和值，遍历nums，在dict_a中查找，如果查找不到当前元素，就把当前元素存储进去，如果查找到则返回
    """

    def twoSum2(self, nums, target):
        dict_a = dict()
        for k, v in enumerate(nums):
            v2 = target - v
            k2 = dict_a.get(v2)
            if k2 is not None:
                return k, k2
            else:
                dict_a[v] = k
        return 0, 0

    def twoSum(self, nums, target):
        dict_num = dict()
        for i, v in enumerate(nums):
            tmp = target - v
            if dict_num.get(tmp) is not None:
                return i, dict_num[tmp]
            else:
                dict_num[v] = i
        return 0, 0


s = Solution()
i1, i2 = s.twoSum(nums, target)
print(i1, i2)
