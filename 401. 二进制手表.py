class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        """
        暴力枚举时间
        """
        r = list()
        if turnedOn >= 9:
            return r
        for h in range(12):
            h_1 = bin(h).count("1")
            for m in range(60):
                m_1 = bin(m).count("1")
                if h_1 + m_1 == turnedOn:
                    r.append(f"{h}:%02d" % m)
        return r


class Solution1:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        r = list()
        if turnedOn >= 9:
            return r
        for i in range(1024):
            h, m = i >> 6, i & 63
            if h < 12 and m < 60:
                if bin(h).count("1") + bin(m).count("1") == turnedOn:
                    r.append(f"{h}:%02d" % m)
        return r
