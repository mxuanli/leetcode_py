class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        r = ""

        def foo(left, right):
            nonlocal r
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            if len(r) < len(s[left + 1: right]):
                r = s[left + 1: right]

        for i in range(n):
            foo(i, i)  # 奇数类型
            foo(i, i + 1)  # 偶数类型
        return r


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
