from collections import defaultdict


class Solution:

    def intersect(self, nums1: list, nums2: list) -> list:
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)
        for num in nums1:
            dict1[num] += 1
        for num in nums2:
            dict2[num] += 1
        r = list()
        for k, v in dict1.items():
            if dict2.get(k):
                for _ in range(min(v, dict2[k])):
                    r.append(k)
        return r

    def run(self):
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]
        r = self.intersect(nums1, nums2)
        print(r)


s = Solution()
s.run()
