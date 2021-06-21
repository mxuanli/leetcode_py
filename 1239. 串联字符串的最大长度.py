class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # 数据量为16、26暴力枚举即可
        str_list = list()
        for a in arr:
            if self.valid_str(a):
                continue
            for s in str_list:
                if not self.valid_str(s + a):
                    str_list.append(s + a)
            str_list.append(a)
        print(str_list)
        r = 0
        for i in str_list:
            r = max(r, len(i))
        return r

    def valid_str(self, text):
        # 是否有重复字符
        if len(set(text)) == len(text):
            return False
        else:
            return True
