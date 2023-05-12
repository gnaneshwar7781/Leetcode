class Solution(object):
    def setZeroes(self, matrix):
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                if matrix[i][j]==0:
                    for k in range(0,len(matrix[i])):
                        if matrix[i][k]!=0:
                            matrix[i][k]='0'

                    for k in range(len(matrix)):
                        if matrix[k][j]!=0:
                            matrix[k][j]='0'



        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                if matrix[i][j]=='0':
                    matrix[i][j]=0
