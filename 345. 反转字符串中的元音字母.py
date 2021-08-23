class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        left, right = 0, n - 1
        vowels_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s_list = list(s)
        while left < right:
            if s_list[left] not in vowels_list:
                left += 1
            if s_list[right] not in vowels_list:
                right -= 1
            if s_list[left] in vowels_list and s_list[right] in vowels_list:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
        return "".join(s_list)


class Solution1:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        left, right = 0, n - 1
        vowels_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s_list = list(s)
        while left < right:
            while left < n and s_list[left] not in vowels_list:
                left += 1
            while right > 0 and s_list[right] not in vowels_list:
                right -= 1
            if left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
        return "".join(s_list)
