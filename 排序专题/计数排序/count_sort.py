'''
计数排序的时间复杂度o(n)
适用于对n个数进行排序，每个数的取值范围是0~n
'''
def count_sort(arr):
    n = len(arr)
    cnt = [0 for i in range(n)]    #  初始化一个长度为n的数组,每个元素的值为0
    for i in range(n):
        cnt[arr[i]] += 1                #  统计每个数出现的次数
    k = 0
    for i in range(n):
        while cnt[i]:                   #  i在数组中出现了不止一次
            arr[k] = i
            k += 1                      #  k后移
            cnt[i] -= 1
    return arr

if __name__ == "__main__":
    arr = [2,1,2,5,6,7,2,3,6]
    print(count_sort(arr))     
               


        

        