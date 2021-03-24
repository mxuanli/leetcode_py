from collections import defaultdict


class Solution:

    def groupAnagrams(self, strs: list) -> list:
        r = defaultdict(list)
        for str_ in strs:
            str_key = "".join(sorted(str_))
            r[str_key].append(str_)
        return list(r.values())

    def run(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        r = self.groupAnagrams(strs)
        print(r)


s = Solution()
s.run()

