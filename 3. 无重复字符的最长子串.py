"""

给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

"""


class Solution(object):

    def lengthOfLongestSubstring2(self, str_s):
        """
        :type s: str
        :rtype: int
        """
        len_str = len(str_s)
        if len_str == 0:
            return 0
        max_str, left, right = 0, 0, -1
        str_dict = dict()
        while True:
            if right + 1 < len_str and str_dict.get(str_s[right+1], 0) == 0:
                str_dict[str_s[right+1]] = 1
                right += 1
            else:
                str_l = str_s[left]
                str_dict[str_l] = 0
                left += 1
            len_i = right - left + 1
            if max_str < len_i:
                max_str = len_i
            if left >= len_str:
                break
        return max_str

    def lengthOfLongestSubstring(self, str_s):
        """
        :type s: str
        :rtype: int
        """
        str_list = list()
        len_str = len(str_s)
        max_len = 0
        for i in range(len_str):
            str_i = str_s[i]
            if str_i in str_list:
                index_i = str_list.index(str_i)
                str_list = str_list[index_i+1:]
            str_list.append(str_i)
            if len(str_list) > max_len:
                max_len = len(str_list)
        return max_len


str_a = "aabaab!bb"


s = Solution()
a = s.lengthOfLongestSubstring(str_a)
print(a)
