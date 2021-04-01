class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        dict_knowledge = dict()
        for i in knowledge:
            dict_knowledge[i[0]] = i[1]
        r = ''
        p1, p2 = 0, 0
        while p2 < len(s):
            if s[p1] == '(':
                while s[p2] != ')':
                    p2 += 1
                r += dict_knowledge.get(s[p1 + 1: p2], '?')
                p1 = p2
            else:
                r += s[p1]
            p1 += 1
            p2 = p1
        return r
