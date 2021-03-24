class Solution:

    def eraseOverlapIntervals(self, intervals: list) -> int:
        if not intervals:
            return 0
        len_intervals = len(intervals)
        intervals.sort()
        i, j, r = 0, 1, 0
        while i < len_intervals and j < len_intervals:
            # 如果左边的右区间大于右边的左区间，则发生重叠，需要移除区间
            if intervals[i][1] > intervals[j][0]:
                # 保留下右区间大的区间
                if intervals[i][1] < intervals[j][1]:
                    i = i - 1  # 左边的小的话，把i-1，后边循环+=1的时候，i就不会变
                else:
                    i = j - 1  # 右边小的话，i = j - 1，后边循环+=1的时候，i会等于现在的j
                r += 1
            else:
                i = j - 1
            i += 1
            j += 1
        return r

    def run(self):
        intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
        r = self.eraseOverlapIntervals(intervals)
        print(r)


s = Solution()
s.run()
