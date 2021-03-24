class Solution:

    def plusOne(self, digits: list) -> list:
        tmp = 0
        digits[-1] += 1
        for i in range(len(digits) - 1, -1, -1):
            num_sum = digits[i] + tmp
            if num_sum >= 10:
                tmp = num_sum // 10
                num_sum = num_sum % 10
            else:
                tmp = 0
            digits[i] = num_sum
        if tmp != 0:
            digits = [tmp] + digits
        return digits

    def run(self):
        digits = [9]
        r = self.plusOne(digits)
        print(r)


s = Solution()
s.run()
