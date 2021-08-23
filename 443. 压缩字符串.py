class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        start, end, write = 0, 0, 0  # start, end开始结束指针，write，写入位置指针
        while end <= n:
            if end == n or chars[start] != chars[end]:
                diff = end - start
                if diff == 1:
                    chars[write] = chars[start]
                    write += 1
                else:
                    chars[write] = chars[start]
                    write += 1
                    for i in list(str(diff)):
                        chars[write] = i
                        write += 1
                start = end
            end += 1
        return write

