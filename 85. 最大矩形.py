class Solution:
    def maximalRectangle(self, matrix: list) -> int:
        width = list()
        maxArea = 0
        for i, iv in enumerate(matrix):
            width.append(list())
            for j, jv in enumerate(iv):
                if jv == '1' and j == 0:
                    width[i].append(1)
                elif jv == '1' and j > 0:
                    width[i].append(width[i][j - 1] + 1)
                else:
                    width[i].append(0)
                min_width = width[i][j]
                for k in range(len(width)):
                    up_row = i - k
                    height = i - up_row + 1
                    min_width = min(min_width, width[up_row][j])
                    maxArea = max(maxArea, height * min_width)
        return maxArea

    def run(self):
        matrix = [["1","0","1","1","1"],["0","1","0","1","0"],["1","1","0","1","1"],["1","1","0","1","1"],["0","1","1","1","1"]]

        r = self.maximalRectangle(matrix)
        print(r)


s = Solution()
s.run()

"""
["1","0","1","1","1"],
["0","1","0","1","0"],
["1","1","0","1","1"],
["1","1","0","1","1"],
["0","1","1","1","1"]
"""
