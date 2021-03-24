class UnionSetFind:

    def __init__(self):
        self.father = dict()
        self.accounts = dict()

    def find(self, x):
        root = x
        # 查找
        while self.father.get(root) is not None:
            root = self.father[root]
        # 压缩
        while x != root:
            father_root = self.father[x]
            self.father[x] = root
            x = father_root
        return root

    def merge(self, x, y):
        # 合并
        xf = self.find(x)
        yf = self.find(y)
        if xf == yf:
            return
        if len(self.accounts[xf]) > len(self.accounts[yf]):
            self.father[yf] = xf
            self.accounts[xf] += self.accounts[yf]
            del self.accounts[yf]
        else:
            self.father[xf] = yf
            self.accounts[yf] += self.accounts[xf]
            del self.accounts[xf]

    def add(self, x):
        # 添加
        if x not in self.father:
            self.father[x] = None
            self.accounts[x] = [x]


class Solution:

    def accountsMerge(self, accounts: list) -> list:
        ufs = UnionSetFind()
        for account in accounts:
            name, root_email = account[0], account[1]
            ufs.add((name, root_email))
            for email in list(set(account[2:])):
                ufs.add((name, email))
                # 如果两个账户都有共同的邮箱地址，在合并的时候，他们的图会被合并到一起
                ufs.merge((name, root_email), (name, email))
        res = list()
        for key in ufs.father.keys():
            if not ufs.father[key]:
                user_accounts = [ufs.accounts[key][0][0]]  # 把name取出来，放在list的第一个
                for account in ufs.accounts[key]:
                    user_accounts += account[1:]
                user_accounts.sort()
                res.append(user_accounts)
        return res

    def run(self):
        accounts = [["Alex", "Alex5@m.co", "Alex4@m.co", "Alex0@m.co"],
                    ["Ethan", "Ethan3@m.co", "Ethan3@m.co", "Ethan0@m.co"],
                    ["Kevin", "Kevin4@m.co", "Kevin2@m.co", "Kevin2@m.co"],
                    ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe2@m.co"],
                    ["Gabe", "Gabe3@m.co", "Gabe4@m.co", "Gabe2@m.co"]]
        r = self.accountsMerge(accounts)
        print(r)


s = Solution()
s.run()
