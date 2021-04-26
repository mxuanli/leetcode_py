class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        start, end = max(weights), sum(weights)
        while start < end:
            mid = start + (end - start) // 2
            days = 1  # 循环到最后的一组days不会加一，所以初始化为1
            r = 0
            # 计算运载能力为mid时候需要的天数
            for weight in weights:
                if r + weight > mid:
                    r = 0
                    days += 1
                r += weight
            if days <= D:
                end = mid
            else:
                start = mid + 1
        return end
