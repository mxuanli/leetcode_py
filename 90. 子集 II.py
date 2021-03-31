import itertools


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result, path = list(), list()
        nums.sort()
        self.foo(result, path, 0, nums)
        return result

    def foo(self, result, path, index, nums):
        result.append(path[:])
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            self.foo(result, path, i + 1, nums)
            path.pop()


class Solution1:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        r = list()
        for i in range(len(nums) + 1):
            r += list(set(itertools.combinations(nums, i)))
        return r
