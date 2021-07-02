class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        r = 0
        if coins < costs[0]:
            return r
        for c in costs:
            if c <= coins:
                coins -= c
                r += 1
            else:
                break
        return r
