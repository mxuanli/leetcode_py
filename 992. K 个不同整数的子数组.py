from collections import defaultdict


class Solution:
    def subarraysWithKDistinct(self, A: list, K: int) -> int:
        nums1 = self.foo(A, K)  # 由最多K个不同整数组成的子数组的个数
        nums2 = self.foo(A, K - 1) # 由最多K-1个不同整数组成的子数组的个数
        return nums1 - nums2

    def foo(self, A: list, K: int) -> int:
        """
        求子数组长度
        :param A:
        :param K:
        :return:
        """
        n = len(A)
        start, end, nums, r = 0, 0, 0, 0
        nums_dict = defaultdict(int)
        for end in range(n):
            num = A[end]
            if nums_dict[num] == 0:
                nums += 1
            nums_dict[num] += 1
            while nums > K:
                num = A[start]
                nums_dict[num] -= 1
                if nums_dict[num] == 0:
                    nums -= 1
                start += 1
            r += end - start + 1  # 子数组个数
        return r

    def run(self):
        A = [1, 2, 1, 2, 3]
        K = 2
        r = self.subarraysWithKDistinct(A, K)
        print(r)


s = Solution()
s.run()
