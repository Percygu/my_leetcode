'''
以小顶堆为例
                0
        1               2
    3       4       5       6
7       8  

'''

# 对数组里的第i个元素向下调整堆-----使堆为小顶堆
def heap_down(arr,size,i):
    t = i
    left,right = 2 * i +1, 2 * i +2            # 左右孩子的下标
    if left < size and arr[left] < arr[t]:     # 当前节点值比左孩子值大，t 变为做孩子下标 ，此时的t是左孩子和跟中的最小者
        t = left
    if right < size and arr[right] < arr[t]:
        t = right                              # 此时的t是左孩子,右孩子还有根中的最小者
    if i != t:                                 # 存在不满足对情况的，需要做调整
        arr[i],arr[t] = arr[t],arr[i]          # 交换根和左右孩子中较小的那一个的值
        heap_down(arr,size,t)                  # 以交换后的节点为根节点，递归向下调整
    

# 对数组里的第i个元素向上调整堆-----使堆为小顶堆
def heap_up(arr,i):
    father = (i-1) // 2                                    # 当前节点的父节点的下标为(i-1) // 2，对顶元素即i为0不需要向上调整了
    while (i-1) // 2 >= 0 and arr[(i-1) // 2] > arr[i]:    # 父节点比当前节点大，不满足小顶堆，需要调整
        arr[i],arr[(i-1) // 2] =   arr[(i-1) // 2],arr[i]  # 只需要交换当前节点和根节点即可，因为原来根节点一定比两个左右孩子小，此时这个孩子碧根节点还小，与根节点交换后，一定比另一个孩子小，不需要调整了
        i = (i-1) // 2 


#  堆排序
def heap_sort(arr):
    n = len(arr)
    # 1.从下往上构建堆，即从数组arr里的每个元素开始一次执行，从下表为1开始
    for i in range(1,n):
        heap_up(arr,i)
    # 把最大元素放到最后面，调整堆
    for i in range(n-1,0,-1):                 #  n表示代派的序列的长度最后一个元素位置，若只有一个对顶元素，则不需要做调整了
    # 2.交换，堆顶元素放到数组末尾 
        arr[0],arr[i] = arr[i],arr[0]         #  把最小的元素放到了数组最后
    # 3.剩下的元素向下调整
        heap_down(arr,i,0)                    #  对数组前面的元素进行向下调整堆操作，调整完之后，对顶就是从整个数组的次小元素，i表示剩余待排元素的个数
    return arr

if __name__ == "__main__":
    arr = [1,4,6,3,7,9,0,2,5,8]
    print(heap_sort(arr))
        
        
    
    







    