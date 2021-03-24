import bisect


class Solution:

    def medianSlidingWindow2(self, nums: list, k: int) -> list:
        start, end = 0, k
        n = len(nums)
        tmp = nums[start: end]
        tmp.sort()
        r_list = list()
        if k % 2 == 0:
            r = (tmp[(k // 2)] + tmp[(k // 2 - 1)]) / 2
        else:
            r = tmp[(k // 2)]
        r_list.append(r)
        for end in range(k, n):
            bisect.insort(tmp, nums[end])
            pop_index = bisect.bisect_left(tmp, nums[start])
            tmp.pop(pop_index)
            if k % 2 == 0:
                r = (tmp[(k // 2)] + tmp[(k // 2 - 1)]) / 2
            else:
                r = tmp[(k // 2)]
            r_list.append(r)
            start += 1
        return r_list

    def medianSlidingWindow(self, nums: list, k: int) -> list:
        start, end = 0, k
        n = len(nums)
        tmp = nums[start: end]
        tmp.sort()
        r_list = list()
        r = self.get_median(tmp, k)
        r_list.append(r)
        for end in range(k, n):
            bisect.insort(tmp, nums[end])
            pop_index = bisect.bisect_left(tmp, nums[start])
            tmp.pop(pop_index)
            r = self.get_median(tmp, k)
            r_list.append(r)
            start += 1
        return r_list

    @staticmethod
    def get_median(tmp: list, k):
        if k % 2 == 0:
            r = (tmp[(k // 2)] + tmp[(k // 2 - 1)]) / 2
        else:
            r = tmp[(k // 2)]
        return r

    def run(self):
        nums = [1, 4, 2, 3]
        k = 4
        r = self.medianSlidingWindow(nums, k)
        print(r)


s = Solution()
s.run()
