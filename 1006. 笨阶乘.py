class Solution:
    def clumsy(self, N: int) -> int:
        i = 0
        key = 2
        stack = list()
        for j in range(N, 0, -1):
            if key == 0:
                stack.append(stack.pop() * j)
            elif key == 1:
                stack.append(int(stack.pop() / j))
            elif key == 2:
                stack.append(j)
            elif key == 3:
                stack.append(0 - j)
            key = i % 4
            i += 1
        return sum(stack)
