class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                del nums[i]
        return len(nums)


class Solution:
    # 双指针
    def removeElement(self, nums: List[int], val: int) -> int:
        start, end = 0, 0
        for end in range(len(nums)):
            if nums[end] != val:
                nums[start] = nums[end]
                start += 1
        return start
