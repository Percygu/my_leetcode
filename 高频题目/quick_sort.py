def quick_sort(nums):
    l,r = 0,len(nums)-1
    sort(nums,l,r)

def sort(nums,l,r):
    if l >= r:
        return
    i = partion(nums,l,r)
    sort(nums,l,i-1)
    sort(nums,i+1,r)

def partion(nums,l,r):
    tmp = nums[l]
    while l < r:
        while l < r and nums[r] >= tmp:
            r -= 1
        nums[l] = nums[r]
        while l < r and nums[l] <= tmp:
            l += 1
        nums[r] = nums[l]
    nums[l] = tmp
    return l



if __name__=="__main__":
    nums = [3,2,1,4,6,5,8,7,9]
    quick_sort(nums)
    print(nums)
