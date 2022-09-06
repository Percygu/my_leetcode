'''
简单计算器3
lc: 772
https://leetcode.cn/problems/basic-calculator-ii/solution/chai-jie-fu-za-wen-ti-shi-xian-yi-ge-wan-zheng-ji-/
'''
class Solution:
    def calculate(self, s: str) -> int:

        # 将字符串变成list处理,操作数总是跟它前面的操作符号绑定，
        def dfs(lists):
            stack = []
            num = 0
            sign = '+'
            while lists:
                c = lists[0]
                del lists[0]
                if c.isdigit():
                    num = num * 10 + int(c)
                if c == '(':
                    num = dfs(s)
                # 本次又遇到了操作符或者是到了字符串尾部,判断上一个操作符的类型，因为每个操作数总数跟他的上一个操作符绑定
                if (not c.isdigit() and c != ' ') or len(s) == 0:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack.append(stack.pop() * num)
                    elif sign == '/':
                        stack.append(stack.pop() / num)
                    num = 0
                    sign = c
                if c == ')':
                    break
            return sum(lists)

        def sum(lists):
            sum = 0
            while lists:
                sum += list.pop()
            return sum

        return dfs(s)











