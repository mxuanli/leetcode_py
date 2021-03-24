class Solution:

    def maxTurbulenceSize2(self, arr: list) -> int:
        n = len(arr)
        if n <= 1:
            return n
        if n == 2:
            if arr[0] == arr[1]:
                return 1
            return n
        count, r = 0, 0
        a, b, c = 0, 1, 2
        if arr[a] == arr[b]:
            count = 1
        else:
            count = 2
        while c < n:
            if arr[a] > arr[b] < arr[c] or arr[a] < arr[b] > arr[c]:
                count += 1
            else:
                if arr[b] == arr[c]:
                    count = max(count, 1)
                else:
                    count = 2
            r = max(count, r)
            a += 1
            b += 1
            c += 1
        return r

    def maxTurbulenceSize(self, arr: list) -> int:
        n = len(arr)
        # 特殊情况
        if n <= 1:
            return n
        if n == 2:
            if arr[0] == arr[1]:
                return 1
            return n
        count, r = 0, 0
        # 前两个值在循环之前判断
        if arr[0] == arr[1]:
            count = 1
        else:
            count = 2
        for i in range(2, n):
            # 判断是不是湍流子数组
            if arr[i - 2] > arr[i - 1] < arr[i] or arr[i - 2] < arr[i - 1] > arr[i]:
                count += 1
            else:
                # 前两个值已经在循环之前或者上一次循环判断过，所以这里只判断后两个值
                if arr[i - 1] == arr[i]:
                    count = 1
                else:
                    count = 2
            # 取最大值
            r = max(count, r)
        return r

    def run(self):
        arr = [0, 1, 1, 0, 1, 0, 1, 1, 0, 0]
        r = self.maxTurbulenceSize(arr)
        print(r)


s = Solution()
s.run()
