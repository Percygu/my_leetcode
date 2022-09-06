class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        visit = [False for _ in range(n)]
        res,path = [],[]
        length = 0
        def dfs(nums,length):
            if length >= n:
                res.append(path[:])
                return
            for i in range(n):
                if visit[i]:
                    continue
                visit[i] = True
                path.append(nums[i])
                dfs(nums,length+1)
                visit[i] = False
                path.pop()

        dfs(nums,0)
        return res

