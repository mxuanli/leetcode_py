
class Solution:

    def isValidSerialization(self, preorder: str) -> bool:
        preorder_list = preorder.split(",")
        stack = [1]
        for pre in preorder_list:
            if not stack:
                return False
            if pre.isdigit():
                stack[-1] -= 1
                if stack[-1] == 0:
                    stack.pop()
                stack.append(2)
            else:
                stack[-1] -= 1
                if stack[-1] == 0:
                    stack.pop()
        if stack:
            return False
        return True

    def run(self):
        preorder = "1,#"
        r = self.isValidSerialization(preorder)
        print(r)


s = Solution()
s.run()
