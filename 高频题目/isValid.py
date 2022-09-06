'''
有效的括号
lc:20
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == '(':
                stack.append(')')
            elif ch == '[':
                stack.append(']')
            elif ch == '{':
                stack.append('}')
            else:
                # 栈为空的情况下来了个右括号,肯定不合法
                if not stack or stack[-1] != ch:
                    return False
                stack.pop()
        return True if not stack else False




