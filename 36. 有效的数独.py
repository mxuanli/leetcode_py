class Solution:

    def isValidSudoku(self, board: list) -> bool:
        n = len(board)
        m = len(board[0])
        row = [[] * 9 for _ in range(9)]
        col = [[] * 9 for _ in range(9)]
        nine = [[] * 9 for _ in range(9)]
        for i in range(n):
            for j in range(m):
                tmp = board[i][j]
                if not tmp.isdigit():
                    continue
                if tmp in row[i]:
                    return False
                if tmp in col[j]:
                    return False
                if tmp in nine[(j // 3) * 3 + (i // 3)]:
                    return False
                row[i].append(tmp)
                col[j].append(tmp)
                nine[(j // 3) * 3 + (i // 3)].append(tmp)
        return True

    def run(self):
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]
        r = self.isValidSudoku(board)
        print(r)


s = Solution()
s.run()
