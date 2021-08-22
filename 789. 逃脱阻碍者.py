class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        # 只要阻碍者可以在你到达终点之前或者同时到达终点，就算输，所以求曼哈顿距离

        def manhattan_distance(x, y):
            # 计算曼哈顿距离
            return abs(x[0] - y[0]) + abs(x[1] - y[1])

        player_distance = manhattan_distance([0, 0], target)
        for ghost in ghosts:
            if manhattan_distance(ghost, target) <= player_distance:
                return False
        return True
