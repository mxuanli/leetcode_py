class Solution:
    def countOfAtoms(self, formula: str) -> str:
        atoms_stack = list()  # 栈，用来存括号里边的内容
        atoms_stack.append(defaultdict(int))  # 第一层
        i = 0
        n = len(formula)
        while i < n:
            s = formula[i]
            # 是大写字母
            if s.isalpha() and s.isupper():
                atoms = s  # 原子名字
                num = 0  # 原子数量
                # 直接循环到下一个原子或者括号（不是大写，也不是括号）
                while i + 1 < n and not formula[i + 1].isupper() and formula[i + 1] not in ["(", ")"]:
                    s = formula[i + 1]
                    # 小写字母就添加到后边
                    if s.islower():
                        atoms += s
                    if s.isdigit():
                        num *= 10
                        num += int(s)
                    i += 1
                # 如果num没有变，就设置为1
                if num == 0:
                    num = 1
                atoms_stack[-1][atoms] += num
            # 括号
            if s == "(":
                # 新的一层
                atoms_stack.append(defaultdict(int))
            if s == ")":
                # 取后边的数字
                i += 1
                num = 0
                while i < n and formula[i].isdigit():
                    num *= 10
                    num += int(formula[i])
                    i += 1
                num = 1 if num == 0 else num
                # 取出计算
                atoms_dict = atoms_stack.pop()
                for k, v in atoms_dict.items():
                    # 括号里边的要乘括号好的数字，并加上上一层的值
                    atoms_stack[-1][k] += (v * num)
                continue
            i += 1
        atoms_dict = atoms_stack[-1]
        keys = sorted(list(atoms_dict.keys()))
        r = ""
        for k in keys:
            if atoms_dict[k] > 1:
                r += "{}{}".format(k, atoms_dict[k])
            else:
                r += k
        return r
