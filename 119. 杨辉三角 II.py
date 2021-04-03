class Solution:

    def getRow(self, rowIndex: int) -> list:
        tmp = [0] * (rowIndex + 1)
        tmp[0] = 1
        for i in range(1, rowIndex + 1):
            for j in range(i, 0, -1):
                tmp[j] += tmp[j - 1]
        return tmp

    def run(self):
        rowIndex = 3
        r = self.getRow(rowIndex)
        print(r)


s = Solution()
s.run()
