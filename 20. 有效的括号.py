class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        dict_s = {"(": ")", "[": "]", "{": "}"}
        for i in s:
            if i in dict_s.keys():
                # 遇到左括号，把对应的右括号压栈
                stack.append(dict_s[i])
            else:
                # 语到左括号判断栈是否为空，或栈内最后一个元素是否和当前字符相等
                if not stack or stack[-1] != i:
                    return False
                stack.pop()
        return len(stack) == 0


