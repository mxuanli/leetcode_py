class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        return S[:length].replace(" ", "%20")


class Solution2:
    def replaceSpaces(self, S: str, length: int) -> str:
        r = ""
        for i in range(length):
            if S[i] == " ":
                r += "%20"
            else:
                r += S[i]
        return r
