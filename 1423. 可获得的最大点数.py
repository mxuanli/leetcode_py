class Solution:

    def maxScore(self, cardPoints: list, k: int) -> int:
        n = len(cardPoints)
        else_len = len(cardPoints) - k  # 计算剩余长度
        start, end = 0, else_len  # 窗口的start和end
        min_else = sum_else = sum(cardPoints[start: end])  # 窗口的初始值
        for end in range(end, n):
            # 移动窗口
            sum_else = sum_else + cardPoints[end] - cardPoints [start]
            min_else = min(sum_else, min_else)  # 比较值
            start += 1
        r = sum(cardPoints) - min_else  # 计算结果
        return r

    def run(self):
        cardPoints = [1, 2, 3, 4, 5, 6, 1]
        k = 3
        r = self.maxScore(cardPoints, k)
        print(r)


s = Solution()
s.run()
