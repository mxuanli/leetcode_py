class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        left, right = 0, n - 1
        r = 0
        while left <= right:
            # 最大的如果不能和最小的一个船，那就只能自己一个船
            if people[left] + people[right] > limit:
                right -= 1
            else:
                # 最大的和最小的一个船，最大利用船空间
                left += 1
                right -= 1
            r += 1
        return r
