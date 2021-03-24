class Solution:

    def lemonadeChange(self, bills: list) -> bool:
        h_bills = dict()
        h_bills[5] = 0
        h_bills[10] = 0
        for bill in bills:
            if bill == 5:
                h_bills[5] += 1
            elif bill == 10:
                if h_bills[5]:
                    h_bills[5] -= 1
                else:
                    return False
                h_bills[10] += 1
            else:
                if h_bills[10] >= 1 and h_bills[5] >= 1:
                    h_bills[10] -= 1
                    h_bills[5] -= 1
                elif h_bills[10] < 1 and h_bills[5] >= 3:
                    h_bills[5] -= 3
                else:
                    return False
        return True

    def run(self):
        bills = [5, 5, 5, 5, 10, 5, 10, 10, 10, 20]
        r = self.lemonadeChange(bills)
        print(r)


s = Solution()
s.run()
