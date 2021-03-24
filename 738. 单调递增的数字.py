class Solution:

    def monotoneIncreasingDigits(self, N: int) -> int:
        list_n = [int(i) for i in str(N)]
        i = 0
        while i < len(list_n)-1:
            if list_n[i] > list_n[i+1]:  # 如果当前的比右边的大，就把当前位-1，把所有右边的位都设置为9
                list_n[i] -= 1
                list_n = list_n[:i+1] + [9 for j in range(len(list_n)-i-1)]
                i = 0  # 重新遍历
                continue
            i += 1
        r = 0
        for i in list_n:
            r *= 10
            r += i
        return r

    def run(self):
        N = 120
        r = self.monotoneIncreasingDigits(N)
        print(r)


s = Solution()
s.run()
