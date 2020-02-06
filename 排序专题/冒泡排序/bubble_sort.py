def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1,0,-1):     # i 取值从arr[n-1]到arr[1]  ,每次选出对的都是剩余元素中最大的的
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
    return arr 
        

#  冒泡排序优化
def bubble_sort1(arr):
    n = len(arr)
    for i in range(n-1,0,-1):     # i 取值从arr[n-1]到arr[1]  ,每次选出对的都是剩余元素中最大的的
        flag = False
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
                flag = True
        if not flag:            #  说明前面都没有发生元素交换，已经都有序了
            break   
    return arr 

#  冒泡排序求逆序对
def bubble_sort2(arr):
    res,n = 0,len(arr)
    for i in range(n-1,0,-1):     # i 取值从arr[n-1]到arr[1]  ,每次选出对的都是剩余元素中最大的的
        flag = False
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
                flag = True
                res += 1
        if not flag:            #  说明前面都没有发生元素交换，已经都有序了
            break   
    return res 
 
if __name__ == "__main__":
    arr = [1,4,6,3,7,9,0,2,5,8]
    print(bubble_sort2(arr))
    