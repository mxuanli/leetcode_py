class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        c_sqrt = int(c ** 0.5) + 1
        for i in range(c_sqrt):
            j2 = c - i ** 2
            if pow(j2, 0.5) == int(pow(j2, 0.5)):
                return True
        return False


class Solution1:
    def judgeSquareSum(self, c: int) -> bool:
        # 假设end永远比start大
        start = 0
        end = int(c ** 0.5) + 1
        while start <= end:
            add = start ** 2 + end ** 2
            if add == c:
                return True
            elif add > c:
                end -= 1
            else:
                start += 1
        return False
