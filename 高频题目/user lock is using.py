'''
解码方法
lc: 91
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for _  in range(len(s)+1)]
        dp[0] = 1        # 第0个字符有一种解码方法,解码成空字符串
        if int(s[0]) == 0:
            dp[1] = 0
        else:
            dp[1] = 1
        for i in range(2,len(s)+1):
            if int(s[i-1]) != 0:
                dp[i] += dp[i-1]
            sub = int(s[i-2:i])
            if sub >=0 and sub <= 26 and int(s[i-2]) != 0:
                dp[i] += dp[i-2]
        return dp[-1]


