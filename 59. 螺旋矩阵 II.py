

class Solution:

    def generateMatrix(self, n: int) -> list:
        r = [[0] * n for _ in range(n)]
        n_list = [i for i in range(n * n, -1, -1)]
        top, right, down, left = 0, n - 1, n - 1, 0
        x, y = 0, -1
        r[x][y] = n_list.pop()
        while n_list:
            while x == top and y < right:
                y += 1
                r[x][y] = n_list.pop()
            top += 1
            while y == right and x < down:
                x += 1
                r[x][y] = n_list.pop()
            right -= 1
            while x == down and y > left:
                y -= 1
                r[x][y] = n_list.pop()
            down -= 1
            while y == left and x > top:
                x -= 1
                r[x][y] = n_list.pop()
            left += 1
        return r

    def run(self):
        n = 3
        r = self.generateMatrix(n)
        print(r)


s = Solution()
s.run()
