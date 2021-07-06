class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        food_list = list()  # 食物列表
        table_food = defaultdict(lambda: defaultdict(int))  # 两层dict，桌子编号和食物数量
        for order in orders:
            _, table, food = order
            # 添加到第一列
            if food not in food_list:
                food_list.append(food)
            table_food[table][food] += 1
        table_list = list(table_food.keys())  # 桌子列表
        food_list.sort()
        table_list.sort(key=int)
        r = list()
        # 添加表头
        r.append(["Table"] + food_list)
        for table in table_list:
            # 添加桌子列
            food_nums = [table]
            # 添加数量列
            for food in food_list:
                food_nums.append(str(table_food[table][food]))
            r.append(food_nums)
        return r

