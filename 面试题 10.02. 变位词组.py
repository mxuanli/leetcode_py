class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r_dict = defaultdict(list)
        for str_ in strs:
            r_dict["".join(sorted(str_))].append(str_)
        r = list(r_dict.values())
        return r
