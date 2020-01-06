#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        k = 0   # k用来记录空格符，因为字符串中可能含有多个连续的空格
        n = len(s)
        for i in range(n):        #从前往后遍历
            while (i<n and s[i] == " "):     #遇到第i个字符是空格，则跳过
                i+=1
            if i == n:
                break              #字符串遍历到头了
            j = i
            while j<n and j!=' ':
                j+=1     #s[i,j)表示一个单词
            s1 = "".join(list(reversed(s[i:j])))
            print(s1)
            if k:
                s[k] = ' '
            while j<i:
                s[k] = s[j]
                j+=1
                k+=1
                       
            
                
                

        
# @lc code=end


'''
思路：
1.先按顺序将每个单词翻转
2，再将整个字符串翻转
'''

