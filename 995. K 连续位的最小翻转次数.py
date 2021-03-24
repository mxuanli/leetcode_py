from collections import deque


class Solution:

    def minKBitFlips(self, A: list, K: int) -> int:
        n = len(A)
        que = deque()  # 下标列表，长度是当前元素被翻转的次数
        r = 0
        for i in range(n):
            if que and que[0] + K <= i:  # 删除超出K范围的元素
                que.popleft()
            if len(que) % 2 == A[i]:  # 如果是0被翻转偶数次还是0，如果是1被翻转奇数次也是0（如果是0则需要翻转）
                if n < i + K:
                    return -1
                que.append(i)
                r += 1
        return r

    def run(self):
        A = [1, 1, 0]
        K = 2
        r = self.minKBitFlips(A, K)
        print(r)


s = Solution()
s.run()
