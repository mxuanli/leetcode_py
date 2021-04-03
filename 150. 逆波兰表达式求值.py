class Solution:
    def evalRPN(self, tokens: list) -> int:
        nums = list()
        count_dict = dict()
        count_dict["+"] = lambda a, b: a + b
        count_dict["-"] = lambda a, b: a - b
        count_dict["/"] = lambda a, b: int(a / b)
        count_dict["*"] = lambda a, b: a * b
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                nums.append(int(token))
            else:
                num1 = nums.pop()
                num2 = nums.pop()
                nums.append(count_dict[token](num2, num1))
        return nums[0]

    def run(self):
        tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        r = self.evalRPN(tokens)
        print(r)


s = Solution()
s.run()
