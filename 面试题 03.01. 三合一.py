class TripleInOne:

    def __init__(self, stackSize: int):
        self.stack = [[] for _ in range(3)]
        self.stackSize = stackSize

    def push(self, stackNum: int, value: int) -> None:
        if len(self.stack[stackNum]) < self.stackSize:
            self.stack[stackNum].append(value)

    def pop(self, stackNum: int) -> int:
        if not self.isEmpty(stackNum):
            return self.stack[stackNum].pop()
        return -1

    def peek(self, stackNum: int) -> int:
        if not self.isEmpty(stackNum):
            return self.stack[stackNum][-1]
        return -1

    def isEmpty(self, stackNum: int) -> bool:
        return len(self.stack[stackNum]) == 0

# Your TripleInOne object will be instantiated and called as such:
# obj = TripleInOne(stackSize)
# obj.push(stackNum,value)
# param_2 = obj.pop(stackNum)
# param_3 = obj.peek(stackNum)
# param_4 = obj.isEmpty(stackNum)
