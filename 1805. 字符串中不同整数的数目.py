class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        tmp = set()
        stack = list()
        for i in word:
            if i.isdigit():
                if len(stack) == 1 and stack[0] == '0':
                    stack.pop()
                stack.append(i)
            else:
                if stack:
                    num = ''.join(stack)
                    tmp.add(num)
                    stack = list()
        if stack:
            num = ''.join(stack)
            tmp.add(num)
        return len(tmp)


