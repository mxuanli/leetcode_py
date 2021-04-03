class Solution:
    def nextGreaterElements1(self, nums: list) -> list:
        r = list()
        for i, num in enumerate(nums):
            flag = False
            new_nums = nums[i:] + nums[:i]
            for num_next in new_nums:
                if num_next > num:
                    r.append(num_next)
                    flag = True
                    break
            if not flag:
                r.append(-1)
        return r

    def nextGreaterElements(self, nums: list) -> list:
        n = len(nums)
        res = [-1] * n
        stack = list()
        for i in range(n * 2):
            # i % n 当前元素的下标
            while stack and nums[stack[-1]] < nums[i % n]:
                res[stack.pop()] = nums[i % n]
            stack.append(i % n)
        return res


    def run(self):
        nums = [1, 2, 3, 4, 5]
        r = self.nextGreaterElements(nums)
        print(r)


s = Solution()
s.run()
