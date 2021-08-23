class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count("A") >= 2:
            return False
        l_count = 0
        for i in s:
            if i == "L":
                l_count += 1
            if i != 'L':
                l_count = 0
            if l_count >= 3:
                return False
        return True


class Solution1:
    def checkRecord(self, s: str) -> bool:
        return s.count("A") < 2 and 'LLL' not in s
