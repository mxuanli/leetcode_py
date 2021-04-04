class Solution(object):
    def numRabbits(self, answers):
        count = collections.Counter(answers)
        return sum((x + y) // (y + 1) * (y + 1) for y, x in count.items())