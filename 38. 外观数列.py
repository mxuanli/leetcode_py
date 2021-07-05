class Solution:
    def countAndSay(self, n: int) -> str:

        def foo(n):
            if n == 1:
                return "1"
            nums_str = foo(n - 1)
            len_nums = len(nums_str)
            this_str = ""
            i = 0
            while i < len_nums:
                num_count = 1
                while i < len_nums - 1 and nums_str[i] == nums_str[i + 1]:
                    num_count += 1
                    i += 1
                this_str += f"{num_count}{nums_str[i]}"
                i += 1
            return this_str

        r = foo(n)
        return r
