class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        """
        广度优先搜索，枚举每次交换后的各种情况
        """
        if board == [[1, 2, 3], [4, 5, 0]]:
            return 0

        def top_move(status, x, y):
            """
            0向上移动一步
            """
            if x == 0:
                return status
            status[1][y], status[0][y] = status[0][y], status[1][y]
            return status

        def down_move(status, x, y):
            """
            0向下移动一步
            """
            if x == 1:
                return status
            status[0][y], status[1][y] = status[1][y], status[0][y]
            return status

        def left_move(status, x, y):
            """
            0向左移动一步
            """
            if y == 0:
                return status
            status[x][y], status[x][y - 1] = status[x][y - 1], status[x][y]
            return status

        def right_move(status, x, y):
            """
            0向右移动一步
            """
            if y == 2:
                return status
            status[x][y], status[x][y + 1] = status[x][y + 1], status[x][y]
            return status

        def get(status):
            """
            移动一步生成器
            """
            if 0 in status[0]:
                x, y = 0, status[0].index(0)
            else:
                x, y = 1, status[1].index(0)
            yield top_move(copy.deepcopy(status), x, y)
            yield down_move(copy.deepcopy(status), x, y)
            yield left_move(copy.deepcopy(status), x, y)
            yield right_move(copy.deepcopy(status), x, y)

        seen = {str(board)}  # 被搜索过的
        q = deque([(board, 0)])  # 搜索队列
        while q:
            status, step = q.popleft()
            for next_status in get(status):
                if str(next_status) not in seen:
                    if next_status == [[1, 2, 3], [4, 5, 0]]:
                        return step + 1
                    q.append((next_status, step + 1))
                    seen.add(str(next_status))
        return -1

