class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        num = (rand7() - 1) * 7 + rand7()       # 可以生成0-49之间的随机数
        while True:
            if num >= 40:
            continue
            return num % 10  + 1
