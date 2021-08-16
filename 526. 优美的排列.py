class Solution:
    def countArrangement(self, n: int) -> int:
        if n <= 3:
            return n
        # 可以满足条件的数预处理
        match = defaultdict(list)
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i % j == 0 or j % i == 0:
                    match[i].append(j)
        self.r = 0
        used = list()

        def foo(i: int):
            # i表示向位置i插入数据
            if i - 1 == n:  # 表示所有位置都存入了数据
                self.r += 1
                return
            for num in match[i]:
                # 找到没用用过的符合条件的数
                if num not in used:
                    used.append(num)
                    foo(i + 1)  # 下一个数字
                    used.pop()  # 回溯

        foo(1)
        return self.r
