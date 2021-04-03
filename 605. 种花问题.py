class Solution:
    def canPlaceFlowers(self, flowerbed: list, n: int) -> bool:
        # 贪心，必要符合条件就种花
        r = 0
        len_f = len(flowerbed)
        for i in range(len_f):
            front, back = 1, 1
            if flowerbed[i] == 0:
                if i == 0:
                    front = 0
                else:
                    front = flowerbed[i - 1]
                if i == len_f -1:
                    back = 0
                else:
                    back = flowerbed[i + 1]
                if front == 0 and back == 0:
                    flowerbed[i] = 1
                    r += 1
        if r >= n:
            return True
        return False

    def run(self):
        flowerbed = [1, 0, 0, 0, 1, 0, 0]
        n = 2
        r = self.canPlaceFlowers(flowerbed, n)
        print(r)


s = Solution()
s.run()
