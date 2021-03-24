class Solution(object):

    @staticmethod
    def reverse(x: int) -> int:
        y = abs(x)
        result = 0
        if x == 0:
            return 0
        elif x > 0:
            max_num = 1 << 31  # 计算32位的值
            while y > 0:
                result = result * 10  # 增加一位
                result += y % 10  # 补上最后一位的值
                y //= 10  # 去除最后一位
                if result > max_num:
                    return 0
            return result
        else:
            max_num = (1 << 31) + 1
            while y > 0:
                result = result * 10  # 增加一位
                result += y % 10  # 补上最后一位的值
                y //= 10  # 去除最后一位
                if result > max_num:
                    return 0
            return 0-result


int_a = -1563847412
s = Solution()
int_b = s.reverse(int_a)
print(int_b)

