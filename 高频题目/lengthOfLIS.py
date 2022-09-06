'''
lc:300
最长递增子序列
'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]   # 表示以下表为i的数字结尾的最长递增序列
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[i - 1]:
                    dp[i] = max(dp[i],dp[j] + 1)
        return max(dp)


