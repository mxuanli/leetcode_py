class Solution:
    def permutation(self, s: str) -> List[str]:
        r = set()
        n = len(s)
        path = ["0" for _ in range(n)]
        vis = [False for _ in range(n)]
        if n == 0:
            return r

        def foo(path: list, vis: list, i: int):
            if i >= n:
                r.add("".join(path))
                return
            for s_i, s_j in enumerate(s):
                if vis[s_i]:
                    continue
                path[i] = s_j
                vis[s_i] = True
                foo(path, vis, i + 1)
                path[i] = "0"
                vis[s_i] = False

        foo(path, vis, 0)
        return list(r)
