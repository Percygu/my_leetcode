'''
回环回原点问题

一、题目描述
一个环，有n个点（编号 0 ~ n-1 ）, 问从0点出发，经过k步回到原点（0点）有多少种方法 ?

二、解题思路 & 代码
再回到 0 点可以从右面回来，也可以从左面回来，即先到达旁边的一个点，看看有多少回来的方法即可。所以运用动态规划的思想，我们可以写出递推式如下：
dp(k,j)=dp(k−1,j−1)+dp(k−1,j+1)

dp(k,j) 表示从点 j 走 k 步到达原点 0 的方法数，

因此可以转化为他相邻的点经过 k − 1 步回到原点的问题，点 j 相邻的点即 j − 1 j 和 j + 1。 这样将问题的规模缩小。

由于是环的问题， j − 1 , j + 1  可能会超出 0 到 n − 1 的范围，因此，我们将递推式改成如下：

d p ( k , j ) = d p ( k − 1 , ( j − 1 + n ) % n ) + d p ( k − 1 , ( j + 1 ) % n )

因为问题从走 k步转化为走 k − 1 k-1k−1 步的问题，所以在写程序的时候我们就按照 k kk 从 0 开始递增的循环写，这样当计算第 k步的时候可以直接使用 k − 1步的结果。
'''


def get_step_num_1(n, k):
    if (n == 0 or n == 1):
        return 1
    # 如果只有n == 2，则偶数有1个方法，奇数不能到达
    if (n == 2):
        if (k % 2 == 0):
            return 1
        else:
            return 0

    dp = [[0] * n for i in range(k + 1)]  # 空间复杂度 O(n * k)

    dp[0][0] = 1
    for i in range(1, n):
        dp[0][i] = 0

    # j is the current step
    for j in range(1, k + 1):
        for i in range(0, n):
            dp[j][i] = dp[j - 1][(i - 1 + n) % n] + dp[j - 1][(i + 1) % n]

    # 这里的0对应的是回到0点，达到任意点可以通过将0改为目标点即可
    return dp[k][0]


def get_step_num_2(n,k):
    if (n == 0 or n == 1):
        return 1
    # 如果只有n == 2，则偶数有1个方法，奇数不能到达
    if (n == 2):
        if (k % 2 == 0):
            return 1
        else:
            return 0

    dp = [[0] * n for i in range(2)]  # 空间复杂度 O(n * 2)

    flag = 1

    dp[0][0] = 1
    for i in range(1, n):
        dp[0][i] = 0

    # j is the current step
    for j in range(1, k + 1):
        for i in range(0, n):
            dp[flag][i] = dp[int(not flag)][(i-1+n) % n] + dp[int(not flag)][(i+1) % n]
        flag = int(not flag)

    # 这里的0对应的是回到0点，达到任意点可以通过将0改为目标点即可
    return dp[int(not flag)][0]


def get_step_num(m,n):
    # m个点，走n步回到原点
    # dp[i][j]表示从原点走i步走到第j个节点的方案数
    # 初始化一个二维数组，行数为走的步数（包含0步），列数为节点个数
    dp = [[0] * m for _ in range(n+1)]
    dp[0][0] = 1  # 从原地走0步到原点有1种方案
    for i in range(1,n+1):  # 走的步数不可能超过n
        for j in range(m):
            dp[i][j] = dp[i-1][(j-1+m)%m] + dp[i-1][(j+1)%m]
    return dp[n][0]



if __name__ == '__main__':
    # n = 102
    # k = 12
    # res1 = get_step_num_1(n, k)
    # res2 = get_step_num_2(n, k)
    # print(res1)
    # print(res2)
    # 10个节点走6步，回到原点
    steps = get_step_num(10,6)
    print(steps)
    steps1 = get_step_num_1(10,6)
    print(steps1)


