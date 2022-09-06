'''
计算器实现(字符串中只包含加减法)
输入：s = "(1+(4+5+2)-3)+(6+8)"
输出：23
lc:224
'''
class Solution:
    def calculate(self, s: str) -> int:
        num,res,sign = 0,0,1
        stack = []
        for c in s:
            # c是数字,求连下一起的数字字符组成的数字
            if c.isdigit():
                num = num * 10 + int(c)
            # 遇到运算符，说明要计算上一段的num
            elif c == '+' or c == '-':
                num *= sign
                sign = 1 if c == '+' else -1   # 更新本次遇到的运算符
                res += num
                num = 0
            # 再碰到左括号之前前面肯定已经遇到过操作符了，所以num已经被置为0了，此时在括号里按照之前没有括号的过程开始计算，所以res要职位0，sign初始化为1
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            # 遇到右括号，说明括号里的计算可以结束了
            elif c == ')':
                # res加上最后一个数字，此时res为括号里的计算结果
                res += num * sign
                res *= stack.pop()   # 当前res带上计算符号
                res += stack.pop()   # 将当前括号里的计算结果加到前面的计算结果中去
                num = 0

        res += num*sign
        return res



