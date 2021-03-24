
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


def isBadVersion(version):
    if version >= 2:
        return True
    return False


class Solution:

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while start <= end:
            mid = start + (end - start) // 2
            if isBadVersion(mid):
                end = mid - 1
            else:
                start = mid + 1
        return start

    def firstBadVersion2(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 0
        end = n
        while start + 1 < end:
            mid = start + (end - start) // 2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid
        if isBadVersion(start):
            return start
        return end

    def run(self):
        n = 2
        r = self.firstBadVersion2(n)
        print(r)


s = Solution()
s.run()
