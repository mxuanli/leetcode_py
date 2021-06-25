class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 广度优先搜索
        if target == "0000":
            return 0
        if "0000" in deadends:
            return -1

        def num_add(num):
            if num == "9":
                return "0"
            return str(int(num) + 1)

        def num_minus(num):
            if num == "0":
                return "9"
            return str(int(num) - 1)

        def get(status):
            """
            返回status被拨动一次后的结果（生成器）
            """
            s = list(status)
            for i in range(4):
                num = s[i]
                s[i] = num_add(num)
                yield "".join(s)
                s[i] = num_minus(num)
                yield "".join(s)
                s[i] = num  # 还原

        seen = {"0000"}  # 被搜索过的
        q = deque([("0000", 0)])  # 搜索队列
        while q:
            status, step = q.popleft()
            for next_status in get(status):
                if next_status not in seen and next_status not in deadends:
                    if next_status == target:
                        return step + 1
                    q.append((next_status, step + 1))
                    seen.add(next_status)
        return -1
