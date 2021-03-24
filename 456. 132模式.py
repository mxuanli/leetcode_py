class Solution:

    def find132pattern_j(self, nums: list) -> bool:
        n = len(nums)
        if n < 3:
            return False
        numi = nums[0]
        for j in range(1, n):
            for k in range(j + 1, n):
                if numi < nums[k] < nums[j]:
                    return True
            numi = min(numi, nums[j])
        return False

    def find132pattern(self, nums: list) -> bool:
        n = len(nums)
        if n < 3:
            return False
        min_left = [float("inf")] * n
        for i in range(1, n):
            min_left[i] = min(min_left[i - 1], nums[i - 1])
        stack = [nums[-1]]
        for j in range(n - 1, -1, -1):
            num_j = nums[j]
            num_k = float("-inf")
            while stack and stack[-1] < num_j:
                num_k = stack.pop()
            if min_left[j] < num_k:
                return True
            stack.append(nums[j])
        return False

    def run(self):
        nums = [3, 1, 4, 2]
        r = self.find132pattern(nums)
        print(r)


s = Solution()
s.run()
