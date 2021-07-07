class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        max_d = max(deliciousness)
        max_d_2 = max_d * 2  # 最大数的二倍，任意两个数的和都不可能超过这个值
        tmp = defaultdict(int)  # 用来存数字数量
        r = 0
        for i in deliciousness:
            sum_d = 1
            while sum_d <= max_d_2:
                r += tmp[sum_d - i]  # 计算当前有几个数字和当前数字相加等于2的幂
                sum_d = sum_d << 1  # 计算2的次幂，范围是从2 - 2 * max
            tmp[i] += 1  # 当前数字数量 + 1
        return r % (10 ** 9 + 7)
