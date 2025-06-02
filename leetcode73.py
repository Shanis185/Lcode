class Solution(object):
    def setZeroes(self, matrix):
        
        row=len(matrix)
        col=len(matrix[0])
        frst_row_zero=any(matrix[0][i]==0 for i in range(col))
        frst_col_zero=any(matrix[i][0]==0 for i in range(row))

        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        if frst_row_zero:
            for i in range(col):
                matrix[0][i]=0
        if frst_col_zero:
            for i in range(row):
                matrix[i][0]=0