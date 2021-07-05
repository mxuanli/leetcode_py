class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        str_one = strs[0]
        for i in str_one:
            common_prefix += i
            for str_i in strs[1:]:
                if not str_i.startswith(common_prefix):
                    return common_prefix[:-1]
        return common_prefix

