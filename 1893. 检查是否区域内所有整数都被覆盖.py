class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        # 暴力
        num_list = list()
        for range_ in ranges:
            start, end = range_[0], range_[1] + 1
            for i in range(start, end):
                num_list.append(i)
        for i in range(left, right + 1):
            if i not in num_list:
                return False
        return True
