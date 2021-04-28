class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        from sortedcontainers import SortedSet
        st = SortedSet()
        start = 0
        for end in range(len(nums)):
            if end - start > k:
                st.remove(nums[start])  # 删除被移除的元素
                start += 1
            i = bisect.bisect_left(st, nums[end] - t)  # 找到适合nums[end] - t插入的第一个位置
            if st and i >=0 and i < len(st) and abs(st[i] - nums[end]) <= t:
                return True
            st.add(nums[end])
        return False
