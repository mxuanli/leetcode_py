import collections
import sys


class Solution:

    def foo(self, nums: list, k: int) -> list:
        if len(nums) < k:
            return max(nums)
        left, right = 0, k
        r_list = list()
        while right <= len(nums):
            k_list = nums[left: right]
            max_num = max(k_list)
            left += 1
            right += 1
            r_list.append(max_num)
        return r_list

    def maxSlidingWindow(self, nums: list, k: int) -> list:
        if len(nums) < k:
            return max(nums)
        r_list = list()
        len_nums = len(nums)
        for i in range(len_nums - k + 1):
            cur = -sys.maxsize
            for j in range(i, i + k):
                cur = max(cur, nums[j])
            r_list.append(cur)
        return r_list

    def maxSlidingWindow2(self, nums: list, k: int) -> list:
        queue = collections.deque()
        r = list()
        len_nums = len(nums)
        for i in range(len_nums):
            # 保持第一个是最大的
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            # 如果最大的不在范围内，就删除掉
            if queue[0] <= i - k:
                queue.popleft()
            if i >= k - 1:
                r.append(nums[queue[0]])
        return r

    def maxSlidingWindow3(self, nums: list, k: int) -> list:
        # 不用双向队列，用list也行
        queue = list()
        r = list()
        len_nums = len(nums)
        for i in range(len_nums):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            if queue[0] <= i - k:
                queue = queue[1:]
            if i >= k - 1:
                r.append(nums[queue[0]])
        return r

    def run(self):
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        r = self.maxSlidingWindow3(nums, k)
        print(r)


s = Solution()
s.run()
