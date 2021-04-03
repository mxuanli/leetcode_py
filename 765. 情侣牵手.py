class Solution:

    def minSwapsCouples2(self, row: list) -> int:
        r, n = 0, len(row)
        for i in range(0, n, 2):
            if row[i] // 2 == row[i + 1] // 2:
                continue
            for j in range(i + 1, n):
                if row[i] // 2 == row[j] // 2:
                    row[i + 1], row[j] = row[j], row[i + 1]
                    r += 1
        return r

    def minSwapsCouples(self, row: list) -> int:
        r, n = 0, len(row)
        for i in range(0, n, 2):
            if row[i] // 2 == row[i + 1] // 2:
                continue
            for j in range(i + 1, n):
                if row[i] // 2 == row[j] // 2:
                    row[i + 1], row[j] = row[j], row[i + 1]
                    r += 1
        return r

    def run(self):
        row = [3, 2, 0, 1]
        r = self.minSwapsCouples(row)
        print(r)


s = Solution()
s.run()
