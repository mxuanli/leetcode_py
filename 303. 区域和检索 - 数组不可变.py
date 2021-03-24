class NumArray2:

    def __init__(self, nums: list):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        r = sum(self.nums[i: j + 1])
        return r


class NumArray:

    def __init__(self, nums: list):
        self.sums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.sums[i + 1] = self.sums[i] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        r = self.sums[j + 1] - self.sums[i]
        return r


n = NumArray([-2, 0, 3, -5, 2, -1])
r = n.sumRange(0, 2)
print(r)
r = n.sumRange(2, 5)
print(r)
r = n.sumRange(0, 5)
print(r)
