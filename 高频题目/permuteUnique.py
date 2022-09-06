'''
lc:47
含有重复数字的全排列
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res,path = [],[]
        n = len(nums)
        visited = [False for _ in range(n)]
        nums.sort()

        def dfs(nums,length):
            if length >= n:
                res.append(path)
                return
            for i in range(n):
                if (i > 0 and not visited[i-1] and nums[i] == nums[i-1]) or visited[i]:
                    continue
                path.append(nums[i])
                visited[i] = True
                dfs(nums,length+1)
                visited[i] = False
                path.pop()
        return res