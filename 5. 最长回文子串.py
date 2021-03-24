class Solution(object):
    def longestPalindrome(self, str_s):
        """
        :type str_s: str
        :rtype: str
        """
        max_str = ""
        len_max_str = 0
        len_str = len(str_s)
        for i in range(len_str):
            left = i
            right = i
            if i < len_str - 1:  # 判断是否到最后一位
                right = i + 1
            if str_s[left] != str_s[right]:  # 相邻的两个是否一样
                if left > 0:  # 判断是否到第一位
                    left -= 1
            while str_s[left] == str_s[right]:
                str_a = str_s[left: right + 1]
                len_str_a = len(str_a)
                if len_str_a > len_max_str:  # 保存最大值
                    len_max_str = len_str_a
                    max_str = str_a
                if left > 0:    # 相邻的两个是否一样
                    left -= 1
                if right < len_str - 1:    # 判断是否到最后一位
                    right += 1
                if left <= 0 and right >= len_str - 1:
                    break
        return max_str


str_s = "aobfboammmqf"
s = Solution()
palindrome = s.longestPalindrome(str_s)
print(palindrome)

"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
"""
