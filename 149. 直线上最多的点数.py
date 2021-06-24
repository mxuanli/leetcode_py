class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        r = 1
        n = len(points)
        # 优化
        if n == 1 or n == 2:
            return n
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                a = x1 - x2
                b = y1 - y2
                tmp = 2
                for z in range(j + 1, n):
                    x3, y3 = points[z]
                    c = x2 - x3
                    d = y2 - y3
                    if a * d == c * b:
                        tmp += 1
                r = max(tmp, r)
                if r > n / 2:  # 优化
                    break
        return r
