class Solution:

    def largeGroupPositions1(self, s: str) -> list:
        left, len_s, r = 0, len(s), list()
        while left < len_s:
            count, l_ = 0, list()
            while left + count < len_s and s[left] == s[left + count]:
                count += 1
            if count >= 3:
                l_.append(left)
                l_.append(left + count - 1)
                r.append(l_)
            left += count
        return r

    def largeGroupPositions(self, s: str) -> list:
        # 双指针
        s += "."
        left, right, r, len_s = 0, 0, list(), len(s)
        for right in range(len_s):
            if s[right] == s[left]:
                continue
            if right - left >= 3:
                r.append([left, right - 1])
            left = right
        return r

    def run(self):
        s = "aaa"
        r = self.largeGroupPositions(s)
        print(r)



s = Solution()
s.run()
