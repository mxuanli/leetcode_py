class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        n = len(citations)
        r = 0
        for h in range(n):
            # 如果论文数大于被引用次数就返回
            if h + 1 > citations[h]:
                break
            r = h + 1
        return r
