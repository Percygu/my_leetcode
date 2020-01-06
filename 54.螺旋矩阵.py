#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix:
            return res
        m,n = len(matrix),len(matrix[0])    #m行n列
        row_1,col_1 = 0,0                   #左上角横纵坐标
        row_2,col_2 = m-1,n-1               #右下角横纵坐标
        while row_1<=row_2 and col_1 <= col_2:
            print("row_1=",row_1,"col_1=",col_1)
            print("row_2=",row_2,"col_2=",col_2)
            for i in range(col_1,col_2+1):
                res.append(matrix[row_1][i])        #打印上面一行
            row_1 +=1
            if row_2 >= row_1:                      #row_2 >= row_1说明矩阵至少两行,才会右边向下打印
                for i in range(row_1,row_2+1):
                    res.append(matrix[i][col_2])    #打印右边一列
            col_2 -=1
            if col_2>=col_1 and row_2 >= row_1:     # clo_2>=clo1说明矩阵至少两列,才会下边向左打印
                for i in range(col_2,col_1-1,-1):
                    res.append(matrix[row_2][i])    #打印下边一行
            row_2 -=1
            if row_2>=row_1 and col_2>=col_1:       #矩阵至少两行三列才会左边向上打印
                for i in range(row_2,row_1-1,-1):
                    res.append(matrix[i][col_1])    #打印左边一列
            col_1 +=1
        return res
        

  
        
# @lc code=end

