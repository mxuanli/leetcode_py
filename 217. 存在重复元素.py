
class Solution:

    def containsDuplicate2(self, nums: list) -> bool:
        return not len(nums) == len(set(nums))

    def containsDuplicate(self, nums: list) -> bool:
        tmp = dict()
        for num in nums:
            if tmp.get(num):
                return True
            tmp[num] = True
        return False

    def run(self):
        nums = [1, 2, 3, 1]
        r = self.containsDuplicate(nums)
        print(r)


s = Solution()
s.run()
