class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) == 0 and len(nums2) == 0:
            return 0
        nums3 = nums1 + nums2
        nums3.sort()
        if len(nums3) % 2 == 0:
            i = len(nums3)//2
            j = len(nums3)//2-1
            return (nums3[i] + nums3[j]) / 2
        elif len(nums3) % 2 == 1:
            i = len(nums3)//2
            return nums3[i]
        else:
            return 0

    def findMedianSortedArrays2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) == 0 and len(nums2) == 0:
            return 0
        i = 0
        j = 0
        k = 0
        len_m = len(nums1) + len(nums2)
        if len_m % 2 == 0:
            pass
        elif len_m % 2 == 1:
            k = len_m // 2
            for i in range(k):
                if i < len(nums1)-1 and nums1[i] <= nums2[j]:
                    i += 1
                else:
                    j += 1
            else:
                if k == j:
                    return nums2[j]
                else:
                    return nums1[i]
        else:
            return 0

    def run(self):
        nums1 = [1, 2]
        nums2 = [3, 4, 5]
        r = self.findMedianSortedArrays2(nums1, nums2)
        print(r)
        # 输出：2.00000
        # 解释：合并数组 = [1, 2, 3] ，中位数


s = Solution()
s.run()
