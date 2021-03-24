
class Solution:

    def calculate(self, s: str) -> int:
        num = 0
        sign = "+"
        s += "a"
        stack = list()
        for i in s:
            if i.isdigit():
                num *= 10
                num += int(i)
            elif i == " ":
                continue
            else:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    stack.append(int(stack.pop() / num))
                num = 0
                sign = i
        return sum(stack)

    def run(self):
        s = "14-3/2"
        r = self.calculate(s)
        print(r)


s = Solution()
s.run()
