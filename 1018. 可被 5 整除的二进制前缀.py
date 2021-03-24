class Solution:

    def prefixesDivBy52(self, A: list) -> list:
        stri = ""
        r_list = list()
        for a in A:
            stri += str(a)
            int10 = int(stri, 2)
            r = False if int10 % 5 else True
            r_list.append(r)
        return r_list

    def prefixesDivBy53(self, A: list) -> list:
        # 判断最后一位是不是0或者5
        n, r_list = 0, list()
        for a in A:
            n = n * 2
            n += a
            n %= 10
            r_list.append(n % 5 == 0)
        return r_list

    def prefixesDivBy5(self, A: list) -> list:
        # 判断最后一位是不是0或者5
        n, r_list = 0, list()
        for a in A:
            n = n * 2
            n += a
            r_list.append(n % 5 == 0)
        return r_list

    def run(self):
        A = [1, 1, 1, 0, 1]
        r = self.prefixesDivBy5(A)
        print(r)


s = Solution()
s.run()
