class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        nums = sorted(intervals,key = itemgetter(0,1),reverse=False)
        cur = nums[0]
        res = []
        for i in range(1,len(nums)):
            if nums[i][0] <= cur[1]:
                start = min(cur[0],nums[i][0])
                end = max(cur[1],nums[i][1])
                cur = [start,end]
            else:
                res.append(cur)
                cur = [nums[i][0],nums[i][1]]
        res.append(cur)
        return res
