class Solution:
    def summaryRanges2(self, nums: list) -> list:
        if not nums:
            return list()
        nums += [min(nums) - 10]
        start = 0
        end = 0
        r_i_list = list()
        for i in range(len(nums)-1):
            if nums[i + 1] != nums[i] + 1:
                r_i_list.append([start, end])
                start = i + 1
                end = i + 1
            else:
                end += 1
        r_s_list = list()
        for r_i in r_i_list:
            r_i_1 = nums[r_i[0]]
            r_i_2 = nums[r_i[1]]
            if r_i_1 != r_i_2:
                rs = str(r_i_1) + "->" + str(r_i_2)
            else:
                rs = str(r_i_1)
            r_s_list.append(rs)
        return r_s_list

    def summaryRanges(self, nums: list) -> list:
        if not nums:
            return list()
        nums += [min(nums) - 10]
        start = 0
        end = 0
        r_s_list = list()
        for i in range(len(nums)-1):
            if nums[i + 1] != nums[i] + 1:
                if start != end:
                    rs = str(nums[start]) + "->" + str(nums[end])
                else:
                    rs = str(nums[start])
                r_s_list.append(rs)
                start = i + 1
                end = i + 1
            else:
                end += 1
        return r_s_list

    def run(self):
        nums = [0, 1, 2, 4, 5, 7]
        r = self.summaryRanges(nums)
        print(r)


s = Solution()
s.run()
