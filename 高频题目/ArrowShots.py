class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        nums = sorted(points,key = itemgetter(0,1),reverse = False)
        cur = nums[0]
        res = 1
        for i in range(1,len(nums)):
            if nums[i][0] <= cur[1]:
                start = max(cur[0],nums[i][0])
                end = min(cur[1],nums[i][1])
                cur = [start,end]
            else:
                cur = [nums[i][0],nums[i][1]]
                res += 1
        return res