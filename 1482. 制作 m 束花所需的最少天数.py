class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m > len(bloomDay) // k:
            return -1

        def foo(days):
            flowers = 0  # 几朵花
            num = 0  # 花束的数量
            for b in bloomDay:
                if b <= days:
                    flowers += 1
                    if flowers == k:
                        num += 1
                        flowers = 0
                        if num == m:
                            return True
                else:
                    flowers = 0
            return num == m

        start, end = min(bloomDay), max(bloomDay)
        while start < end:
            mid = start + (end - start) // 2
            if foo(mid):
                end = mid
            else:
                start = mid + 1
        return start
