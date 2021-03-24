

class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        i = 0
        while i < len(haystack)-len(needle)+1:
            j = 0
            while j < len(needle):
                if haystack[i+j] != needle[j]:
                    break
                j += 1
            if len(needle) == j:
                return i
            i += 1
        return -1

    def run(self):
        haystack = "h"
        needle = "h"
        r = self.strStr(haystack, needle)
        print(r)


s = Solution()
s.run()
