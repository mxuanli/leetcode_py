class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        tmp = map(str, nums)
        tmp = sorted(tmp, key=cmp_to_key(self.compare))
        if tmp[0] == "0":
            return "0"
        return "".join(tmp)

    def compare(self, x, y):
        if x + y < y + x:
            return 1
        else:
            return - 1
