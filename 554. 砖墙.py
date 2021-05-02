class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        wall_hash = defaultdict(int)
        for wa in wall:
            add = 0
            for w in wa:
                add += w
                wall_hash[add] += 1
        n = len(wall)
        m = sum(wall[0])
        wall_hash[m] = 0
        max_wall = max(wall_hash.values())
        r = n - max_wall
        return r
