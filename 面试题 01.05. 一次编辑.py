from collections import defaultdict


class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        if len(first) < len(second):
            first, second = second, first
        if abs(len(first) - len(second)) > 1:
            return False
        for i in range(len(second)):
            if first[i] != second[i]:
                if len(first) != len(second):
                    if first[i + 1:] != second[i:]:
                        return False
                else:
                    if first[i + 1:] != second[i + 1:]:
                        return False
        return True


s = Solution()
r = s.oneEditAway("teacher", "bleacher")
print(r)

print("ab"[1:])
print("bc"[1:])
