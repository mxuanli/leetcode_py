class Solution:
    def smallestGoodBase(self, n: str) -> str:
        """
        把解体思路变成,求由 N 个 1 组成的字符串，转换成n所需要的进制k
        然后从n的二进制位数个1，遍历到0个1，如果正好有一个由 N 个 1组成的字符串转换为k进制之后的值为n，就返回这个k
        """
        n = int(n)
        # 进制越大，转换后就越短，所以最长是二进制（1进制值都是0）
        binary_system_len = len(bin(n)) - 2
        for N in range(binary_system_len, 0, -1):
            start = 2  # 最低是2进制
            end = n - 1  # 最高是 n-1 进制
            while start <= end:
                mid = start + (end - start) // 2
                v = self.sum_with(mid, N)
                # 进制越小，转换后的数字就越小，进制越大转换后的数字就越大（2进制的111转换为十进制后为7，8进制转换后为73）
                # 所以如果 v < n，需要加大进制
                if v < n:
                    start = mid + 1
                elif v > n:
                    end = mid - 1
                else:
                    return str(mid)

    def sum_with(self, base, N):
        """
        # N个1组成的，base进制数字转换为10进制
        :param base:，转换之前的进制
        :param N，base进制的位数，表示N个1
        """
        return (1 - base ** N) // (1 - base)
