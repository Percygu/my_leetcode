'''
单词拆分
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        回溯划分单词
        '''
        marked = {}  # 用于标记那些字符串不能够有效拆分，避免重复计算
        def dfs(s):
            res = False   # 默认不能正确拆分
            if not s:   # 字符串被拆分完了
                return True
            if s in marked:
                return False
            for i in range(len(s)):
                sub = s[:i+1]
                rest = s[i+1:]
                if sub in wordDict:
                    flag = dfs(rest)
                    if not flag:
                        marked[rest] = False
                    res = res or flag   # 只要有一组可以满足就可以正确拆分，所以用or，不用and
            return res
        return dfs(s)

