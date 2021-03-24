from collections import defaultdict


class Solution:

    def findShortestSubArray2(self, nums: list) -> int:
        dict1 = defaultdict(int)
        dict2 = dict()
        for i, num in enumerate(nums):
            dict1[num] += 1
            if not dict2.get(num):
                dict2[num] = [i, i, 1]
            else:
                dict2[num][1] = i
                dict2[num][2] = dict2[num][1] - dict2[num][0] + 1
        tmp = sorted(dict1.items(), key=lambda kv: (kv[1]), reverse=True)
        degree = tmp[0][1]
        r = 50001
        for k, v in dict1.items():
            if v == degree:
                r = min(dict2[k][2], r)
        return r

    def findShortestSubArray(self, nums: list) -> int:
        dict1 = dict()
        for i, num in enumerate(nums):
            if not dict1.get(num):
                dict1[num] = [1, i, i]
            else:
                dict1[num][0] += 1
                dict1[num][2] = i
        tmp = sorted(dict1.items(), key=lambda kv: (kv[1][0]), reverse=True)
        r = 50001
        degree = tmp[0][1][0]
        for k, v in dict1.items():
            if v[0] == degree:
                r = min(r, v[2] - v[1] + 1)
        return r

    def run(self):
        nums = [1, 2, 2, 3, 1]
        r = self.findShortestSubArray(nums)
        print(r)


s = Solution()
s.run()
