class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        node = label
        r = list()
        # 计算是在第几行，求2的对数，然后+1
        n = int(log2(label)) + 1
        while n > 0:
            # 添加到返回值
            r.append(node)
            # 计算对称节点
            if n % 2 == 0:
                # 反向
                start, end = (2 ** n) - 1, 2 ** (n - 1)
                symmetry = end + (start - node)
            else:
                # 正向
                start, end = 2 ** (n - 1), (2 ** n) - 1
                symmetry = end + (start - node)
            # 计算父节点
            node = symmetry // 2
            n -= 1
        return r[::-1]
