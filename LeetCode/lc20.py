# class Solution:   单种括号匹配
#     def isValid(self, s):
#         left = 0
#         for i in range(len(s)):
#             if(s[i] == '('):
#                 left += 1
#             else:
#                 left -= 1
#         return True if left == 0 else False

# Runtime: 44 ms, faster than 45.12%    多种括号匹配
# 思路：初始化栈 S。如果遇到左括号，将其推到栈顶。如果遇到右括号，那么检查栈顶元素。如果栈顶的元素是一个相同类型的左括号，那么将它从栈中弹出并继续处理。
# 否则，意味着表达式无效。如果到最后剩下的栈中仍然有元素，那么这意味着表达式无效。

class Solution:
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False    # 若出现括号以外的非法字符，返回False
        return stack == []  # 若stack为空则返回True，否则返回False

if __name__ == '__main__':
    s = '((([[]]{})))'
    print(Solution().isValid(s))