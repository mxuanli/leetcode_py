class Solution:

    def countBits2(self, num: int) -> list:
        r = list()
        for i in range(num + 1):
            bit = str(bin(i)).count("1")
            r.append(bit)
        return r

    def countBits(self, num: int) -> list:
        r = list()
        for i in range(num + 1):
            count = 0
            while i != 0:
                i &= (i - 1)
                count += 1
            r.append(count)
        return r

    def run(self):
        num = 5
        r = self.countBits(num)
        print(r)


s = Solution()
s.run()
