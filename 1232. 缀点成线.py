class Solution:
    def checkStraightLine(self, coordinates: list) -> bool:
        x, y = coordinates[0][0], coordinates[0][1]
        x1 = coordinates[1][0] - x
        y1 = coordinates[1][1] - y
        for i, j in coordinates[2:]:
            xi = i - x
            yj = j - y
            if x1 * yj - y1 * xi:
                return False
        return True

    def run(self):
        coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
        r = self.checkStraightLine(coordinates)
        print(r)


s = Solution()
s.run()
