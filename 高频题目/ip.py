class Solution:
    def restoreIpAddresses(self, s: str):
        res,path = [],[]
        def dfs(s,pos,i):
            if i >= 4:
                res.append('.'.join(path[:]))
                return
            for i in range(0,3):
                if pos + i >= len(s):
                    break
                sub = s[pos,pos+i+1]
                if i >= 1 and (s[pos] == '0' or int(sub) > 255):
                    continue
                path.append(sub)
                dfs(s,pos+i+1,i+1)
                path.pop(-1)
        dfs(s,0,0)
        return res