

class Solution:

    def predictPartyVictory(self, senate: str) -> str:
        total_r, total_d, ban_r, ban_d, total_ban_r, total_ban_d, k = 0, 0, 0, 0, 0, 0, False
        senate_list = list(senate)
        while True:
            for i in range(len(senate_list)):
                if senate_list[i] == "R":
                    if ban_r > 0:
                        senate_list[i] = "r"  # 如果当前角色被ban，则设置为r，后边不参与计算
                        ban_r -= 1
                    else:
                        ban_d += 1  # 如果没被ban，就ban对方的角色
                        total_ban_d += 1
                    if not k:
                        total_r += 1  # 计算阵营人数
                elif senate_list[i] == "D":
                    if ban_d > 0:
                        senate_list[i] = "d"
                        ban_d -= 1
                    else:
                        ban_r += 1
                        total_ban_r += 1
                    if not k:
                        total_d += 1
            k = True  # 只有第一轮会计算阵营人数
            if total_ban_r > total_r:
                return "Dire"
            if total_ban_d > total_d:
                return "Radiant"

    def run(self):
        senate = "RD"
        r = self.predictPartyVictory(senate)
        print(r)


s = Solution()
s.run()
