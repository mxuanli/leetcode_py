class Solution:

    def candy(self, ratings: list) -> int:
        # 满足左规则的最优解
        left_list = [1 for _ in ratings]
        for i in range(1, len(left_list)):
            if ratings[i] > ratings[i - 1]:
                left_list[i] = left_list[i - 1] + 1
        # 满足右规则的最优解
        right_list = [1 for _ in ratings]
        for i in range(len(right_list) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right_list[i] = right_list[i + 1] + 1
        # 合并之后的最大值就是同时满足左和右的最优解
        count = 0
        for i in range(len(ratings)):
            count += max(left_list[i], right_list[i])
        return count

    def run(self):
        ratings = [1, 2, 87, 87, 87, 2, 1]
        r = self.candy(ratings)
        print(r)


s = Solution()
s.run()
