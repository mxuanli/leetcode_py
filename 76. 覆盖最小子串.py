from collections import defaultdict


class Solution:

    def minWindow(self, s: str, t: str) -> str:
        result = ""
        if len(s) == 0 or len(s) < len(t):
            return result
        s_dict = dict()
        t_dict = dict()
        for i in t:
            t_dict[i] = t_dict.get(i, 0) + 1
        left, right, last_left, last_right, count, min_win = 0, -1, -1, -1, 0, len(s)+1
        while left < len(s):
            if count < len(t) and right+1 < len(s):
                s_dict[s[right+1]] = s_dict.get(s[right+1], 0) + 1
                if s_dict.get(s[right+1], 0) <= t_dict.get(s[right+1], 0):
                    count += 1
                right += 1  # 增大窗口
            else:
                if right + 1 - left < min_win and count == len(t):
                    last_left = left
                    last_right = right + 1
                    min_win = right + 1 - left
                if s_dict.get(s[left], 0) == t_dict.get(s[left], 0):
                    count -= 1
                s_dict[s[left]] = s_dict.get(s[left], 0) - 1
                left += 1  # 缩小窗口
        if last_left != -1:
            result = s[last_left: last_right]
        return result

    def minWindow2(self, s: str, t: str) -> str:
        result = ""
        if len(s) == 0 or len(t) == 0:
            return result
        freq = defaultdict(int)
        for c in t:
            freq[c] += 1
        left, right, last_left, last_right, count = 0, 0, -1, len(s), len(t)
        for right, c in enumerate(s):
            if freq[c] > 0:
                count -= 1
            freq[c] -= 1
            if count == 0:
                while True:
                    c = s[left]
                    if freq[c] == 0:
                        count += 1
                        break
                    freq[c] += 1
                    left += 1
                if right - left < last_right - last_left:
                    last_right = right
                    last_left = left
                freq[c] += 1
                left += 1
        if last_left != -1:
            result = s[last_left: last_right+1]
        return result

    def run(self):
        S = "bdab"
        T = "ba"
        result = self.minWindow2(S, T)
        print(result)


s = Solution()
s.run()
