class Solution:
    def canCross(self, stones: List[int]) -> bool:
        set_stones = set(stones)

        @functools.lru_cache(maxsize=None, typed=False)
        def foo(stone, step):
            """
            在经过step步的跳跃到达stone之后是否可以到达终点
            :param stone: 第几块石头
            :param step: 跳了多少步
            :return:
            """
            if stone == stones[-1]:  # 到达了终点
                return True
            for i in [-1, 0, 1]:
                if step + i >= 1 and stone + step + i in set_stones:
                    if foo(stone + step + i, step + i):
                        return True
            return False

        return foo(0, 0)


class Solution1:
    def canCross(self, stones: List[int]) -> bool:
        set_stones = set(stones)
        hash_map = dict()

        def foo(stone, step):
            """
            在经过step步的跳跃到达stone之后是否可以到达终点
            :param stone: 第几块石头
            :param step: 跳了多少步
            :return:
            """
            if (stone, step) in hash_map:
                return hash_map.get((stone, step))
            if stone == stones[-1]:  # 到达了终点
                return True
            for i in [-1, 0, 1]:
                if step + i >= 1 and stone + step + i in set_stones:
                    if foo(stone + step + i, step + i):
                        hash_map[(stone, step)] = True
                        return True
            hash_map[(stone, step)] = False
            return False

        return foo(0, 0)

