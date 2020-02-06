'''
基数排序(桶排序)
假设数组中最大的数只有3位
分为3个桶，个位，十位，百味
'''

# 获取数字x对应位数的值
def get(x,i):            # i =0,返回x个位上的数，i=1，返回x10位上的数，i=2，返回x百位上的数...
    while i:
        x //= 10
        i -= 1
    return x % 10

def base_sort(arr):
    n = len(arr)
    cnt = [[] for i in range(10)]    # 开一个 10 * 10，初始化为0的二维数组
    for i in range(3):                     #  按个位，十位，百位各排一次
        for k in range(10):
            cnt[k] = []              #  把十个桶，每个桶置空,因为低位排完之后，0-9对的10个桶体里都有了值
        for j in range(n):
            cnt[get(arr[j],i)].append(arr[j])  # cnt[get(arr[j]),i]是一个以为数组，get(arr[j])取值相同的都加入到这个数组中
        #  排序
        k = 0
        for j in range(10):         # 从当前为最次奥德是即0开始往后，依次到9
            for x in cnt[j]:        # 该位数值相同  有多个数，则k往后移
                arr[k] = x
                k += 1
    return arr

if __name__ == "__main__":
    arr = [564,32,123,98,12,9,123,987,544,763]
    print(get(564,0))
    print(base_sort(arr))

