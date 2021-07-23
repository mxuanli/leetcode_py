class CQueue:

    def __init__(self):
        self.stack1 = list()
        self.stack2 = list()

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)
        self.stack2 = self.stack1[::-1]

    def deleteHead(self) -> int:
        if not self.stack2:
            return -1
        r = self.stack2.pop()
        self.stack1 = self.stack2[::-1]
        return r

    # Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
