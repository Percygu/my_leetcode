class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        prefix = 1
        while k > 1:
            cnt = self.get_num(prefix,n)
            if(cnt > k):
                prefix *= 10   # 往后移动一个数字
                k -= 1
            else:
                prefix += 1
                k += cnt
        return prefix

    def get_num(self,prefix,n):
        next = prefix + 1
        cnt = 0
        while prefix < n:
            cnt += min(next,n+1) - prefix
            prefix *= 10
            next *= 10
        return cnt




